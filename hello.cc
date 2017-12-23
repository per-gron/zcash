#include <stdio.h>
#include <event2/event.h>
#include <db_cxx.h>
#include <gmp.h>
#include <sodium.h>
#include <zmq.h>
#include <proton/connection.hpp>
#include <openssl/crypto.h>

int main() {
  CRYPTO_num_locks();
  printf("hello\n");
  return 0;
}
