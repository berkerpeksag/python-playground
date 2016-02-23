"""
Simple forking echo server built with Python's SocketServer library. A more
Pythonic version of http://gist.github.com/203520, which itself was inspired
by http://tomayko.com/writings/unicorn-is-unix.
"""

import os
import socketserver


class EchoHandler(socketserver.StreamRequestHandler):
    def handle(self):
        self.wfile.write('Child {} echo>'.format(os.getpid()).encode())
        self.wfile.flush()
        message = self.rfile.readline()
        self.wfile.write(message)
        print("Child {} echo'd: {!r}".format(os.getpid(), message))

if __name__ == '__main__':
    server = socketserver.ForkingTCPServer(('localhost', 4242), EchoHandler)
    print("Server listening on localhost:4242...")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nbailing...")
