def main():
    for num in xrange(1, 101):
        msg = ''
        if num % 3 == 0:
            msg += 'Fizz'
        if num % 5 == 0:
            msg += 'Buzz'
        print msg or num

if __name__ == '__main__':
    main()
