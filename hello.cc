#include <stdio.h>
#include <event2/buffer.h>
#include <db_cxx.h>
#include <gmp.h>
#include <sodium.h>
#include <zmq.h>
#include <proton/connection.hpp>
#include <openssl/crypto.h>

int main() {
  CRYPTO_num_locks();
  evbuffer_commit_space(nullptr, nullptr, 0);
  printf("hello\n");
  return 0;
}
