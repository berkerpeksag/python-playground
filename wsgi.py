from __future__ import print_function


class Application(object):

    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-type', 'text/plain')])
        return ['Cardinal Biggles.']


if __name__ == '__main__':
    import sys
    import wsgiref.simple_server

    try:
        port = int(sys.argv[1])
    except (IndexError, ValueError):
        port = 8005
    print('Serving on port %d...' % port)
    try:
        httpd = wsgiref.simple_server.make_server('', port, Application())
        httpd.serve_forever()
    except KeyboardInterrupt:
        print()
        print('Closing...')
        httpd.shutdown()
        sys.exit(1)
