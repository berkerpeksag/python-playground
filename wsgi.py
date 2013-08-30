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
    httpd = wsgiref.simple_server.make_server('', port, Application())
    httpd.serve_forever()
