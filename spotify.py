"""
Solutions of Spotify's Tech Puzzles in Python 3

https://www.spotify.com/fi/jobs/tech/

"""

def reversebinary(n):
    """Return the number we get by reversing the binary representation of N.

    See for more info: https://www.spotify.com/fi/jobs/tech/reversed-binary/

    """
    return int(bin(n)[:1:-1], 2)

if __name__ == '__main__':
    import sys

    print(reversebinary(int(sys.argv[1])))
