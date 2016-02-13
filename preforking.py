import os
import socket
import signal

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 9999))
s.listen(1)

wpids = []


def handler(signum, frame):
    for pid in wpids:
        os.kill(pid, signum)

for sig in [signal.SIGINT, signal.SIGQUIT]:
    signal.signal(sig, handler)

for _ in range(5):
    pid = os.fork()
    if pid != 0:
        wpids.append(pid)
        while True:
            conn, addr = s.accept()
            conn.sendall(b"Hello Readers!\n")
            conn.close()

try:
    while True:
        wpid, status = os.waitpid(-1, os.WNOHANG)
        if not wpid:
            break
except ChildProcessError:
    pass
