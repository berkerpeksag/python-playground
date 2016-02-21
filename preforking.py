import os
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 9999))
s.listen(10)

for _ in range(5):
    pid = os.fork()
    if pid == 0:
        cpid = os.getpid()
        try:
            while True:
                conn, addr = s.accept()
                conn.sendall(b"Hello Readers!\n")
                conn.close()
        except KeyboardInterrupt:
            print('bailing child {}...'.format(cpid))
            sys.exit()

try:
    os.waitpid(-1, 0)
except KeyboardInterrupt:
    print("bailing...")
    sys.exit()
