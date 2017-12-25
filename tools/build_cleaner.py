# Find relevant targets: bazel query //src/...
# Generate full dependency graph: bazel query --output xml --xml:default_values 'deps(//src/...)'

import os
import re
import xml.etree.ElementTree as ET

def get_target_tags(root):
    """Get a dict of all target names to their XML tag in the input data."""
    tags = {}
    for child in root:
        tags[child.attrib["name"]] = child
    return tags

def should_process_target(target_tags, name):
    """Returns True if the target is one that should be cleaned."""
    tag = target_tags[name]
    return name.startswith("//src/") and tag.tag == 'rule'

def extract_label_list(target_tag, name):
    """For a given target XML tag and a name, for example 'deps' or 'srcs',
    extract the list of labels in that list."""
    for child in target_tag:
        if child.tag == "list" and child.attrib["name"] == name:
            return [c.attrib["value"] for c in child]
    return []  # Not found

def rule_input_labels(target_tag):
    """Given a target XML tag, get a list of labels for the files that are
    directly included in that target."""
    return list(set(
        extract_label_list(target_tag, "srcs") + \
        extract_label_list(target_tag, "textual_hdrs") + \
        extract_label_list(target_tag, "hdrs")))

def rule_headers_labels(target_tag):
    """Given a target XML tag, get a list of labels for the files that are
    directly included in that target."""
    return list(set(
        extract_label_list(target_tag, "textual_hdrs") + \
        extract_label_list(target_tag, "hdrs")))

def rules_input_labels(target_tags):
    """Like rule_input_labels, but for a dict of targets instead of just one
    target."""
    res = {}
    for name in target_tags:
        res[name] = rule_input_labels(target_tags[name])
    return res

def get_rule_hdr_bazelpaths(target_tags):
    """Returns a dict from Bazel paths (for example //src/a.h or @boost//a/b.h)
    to the name of the rule that exports that header."""
    res = {}
    for name in target_tags:
        for hdr in rule_headers_labels(target_tags[name]):
            bazel_path = hdr.replace(":", "/").replace("///", "//")
            if bazel_path not in res:
                res[bazel_path] = []
            res[bazel_path] += [name]
    return res

def get_workspace_dir():
    workspace_dir = os.getcwd()
    while workspace_dir != os.path.dirname(workspace_dir):
        if os.path.isfile(os.path.join(workspace_dir, "WORKSPACE")):
            return workspace_dir
        workspace_dir = os.path.dirname(workspace_dir)
    raise Exception("It seems like this script is not run within a Bazel workspace")

def label_to_path(workspace_dir, label):
    if not label.startswith('//'):
        raise Exception("%s is not an absolute label", label)
    return os.path.join(workspace_dir, label[2::].replace(':', '/'))

include_regex = re.compile(r'^\s*#\s*[Ii][Nn][Cc][Ll][Uu][Dd][Ee]\s*"(.*)"\s*$')
def extract_nonsystem_includes(path):
    """Return a set of paths (relative to whatever the header search paths are)
    that are #include-d by the file at the given path."""
    res = set()
    if not os.path.isfile(path):
        # This could be the output of a genrule. In that case we simply assume
        # that the genrule has properly declared dependencies and ignore this.
        return res

    with open(path, "r") as f:
        for line in f.readlines():
            match = re.match(include_regex, line)
            if match:
                res.add(match.group(1))
        return res

def extract_nonsystem_includes_of_target(workspace_dir, rule_input_labels, name):
    """Return a set of paths (relative to whatever the header search paths are)
    that are #include-d by all the files of the given target."""
    res = set()
    for label in rule_input_labels[name]:
        if label.startswith('@bazel_tools//'):
            continue
        res = res.union(extract_nonsystem_includes(label_to_path(workspace_dir, label)))
    return res

def get_header_search_paths(target_tags):
    """Returns a dict of target name to a set of header search Bazel-paths (for
    example //src/abc or @boost//) that are used when compiling files in that
    target."""

    # This is configured in tools/bazel.rc, which this script doesn't see
    builtin_search_paths = ["//src"]

    def empty_if_just_dot(path):
        if path == ".":
            return ""
        elif path.endswith('/') and not path == "/":
            return path[:-1]
        else:
            return path

    res = {}
    def process_target(name):
        target_tag = target_tags[name]
        if name in res or target_tag.tag != "rule":
            return
        target_workspacename = name.split("//")[0]
        target_dirname = name.split(":")[0]
        if not target_dirname.endswith("/"):
            target_dirname += "/"
        paths = set(builtin_search_paths + [target_workspacename + "//"])
        for dir in extract_label_list(target_tag, "includes"):
            paths.add(target_dirname + empty_if_just_dot(dir))
        for copt in extract_label_list(target_tag, "copts"):
            if not copt.startswith("-I"):
                continue
            path = copt[2:]
            path = re.sub(r'^\$\(GENDIR\)\/', '', path)
            if path.startswith('external/'):
                paths.add(re.sub(r'^external\/([^\/]+)\/', r'@\1//', path))
            else:
                paths.add('//' + path)
        for dep in extract_label_list(target_tag, "deps"):
            process_target(dep)
            paths = paths.union(res[dep])
        res[name] = paths
    for name in target_tags:
        process_target(name)
    return res

def resolve_included_header(hdr_bazelpaths, target_name, search_paths, path):
    for search_path in search_paths:
        bazelpath = "%s/%s" % (search_path, path)
        if bazelpath in hdr_bazelpaths:
            return hdr_bazelpaths[bazelpath]

    # Not found. Perhaps the header search path is relative to the file path?
    bazelpath = re.sub(r"/[^\/]*$", r"/", target_name.replace(":", "/")) + path
    if bazelpath in hdr_bazelpaths:
        return hdr_bazelpaths[bazelpath]

    print "LOL!!! TODO(per-gron) %s - %s - %s" % (target_name, path, bazelpath)
    return set()
    raise Exception("Could not resolve header %s for target %s", path, target_name)


tree = ET.parse("all_deps.xml")
root = tree.getroot()

"""Path of whatever is called // in the BUILD files"""
workspace_dir = get_workspace_dir()
"""Dict of all target names to their target XML tags."""
target_tags = get_target_tags(root)
"""Dict of all target names to labels of the directly included files."""
rule_input_labels = rules_input_labels(target_tags)
"""Dict of all Bazel paths to the target name that exports them."""
rule_hdr_bazelpaths = get_rule_hdr_bazelpaths(target_tags)
"""List of all target names that should be cleaned."""
target_names_to_process = \
    [name for name in target_tags.keys() if should_process_target(target_tags, name)]
"""Dict of all target names to Bazel paths of header search paths."""
target_search_paths = get_header_search_paths(target_tags)

# With include search paths and #include statements, a list of included files can be retrieved
# With that we can get what targets each target actually depends on
# The actual deps and the calculated deps are then compared

#for name in target_names_to_process:
#    print name, rule_input_labels[name]

#for name in target_names_to_process:
#    print name, target_search_paths[name]

#print rule_hdr_bazelpaths

#for name in target_names_to_process:
#    print name, target_search_paths[name], extract_nonsystem_includes_of_target(workspace_dir, rule_input_labels, name)

for name in target_names_to_process:
    search_paths = target_search_paths[name]
    resolved_headers = [resolve_included_header(rule_hdr_bazelpaths, name, search_paths, header) for header in extract_nonsystem_includes_of_target(workspace_dir, rule_input_labels, name)]
    # print name, search_paths, resolved_headers
