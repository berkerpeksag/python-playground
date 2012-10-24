import sys
import tokenize


def main(filename):
    reader = open(filename, 'r').readline
    for typ, tok, (sr, sc), (er, ec), line in tokenize.generate_tokens(reader):
        print type, tok, (sr, sc)

if __name__ == '__main__':
    main(sys.argv[1])
