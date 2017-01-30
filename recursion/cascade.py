# http://composingprograms.com/pages/17-recursive-functions.html


def cascade(n):
    if n < 10:
        print('-', n)
    else:
        print('+', n)
        cascade(n // 10)
        # Until the return value appears (which is None in this case)
        # that call has not completed.
        #
        # 123 -> 1st call, first print
        # 12  -> 2nd call, first print
        # 1   -> 3rd call, base case print
        # 12  -> 2nd call, second print
        # 123 -> 1nd call, second print
        print('*', n)


# It is not a rigid requirement that base cases be expressed before recursive
# calls. In fact, this function can be expressed more compactly by observing
# that print(n) is repeated in both clauses of the conditional statement.
def cascade2(n):
    print('-+', n)
    if n > 10:
        cascade2(n // 10)
        print('*', n)


def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)


def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

if __name__ == '__main__':
    cascade(1234)
    print('-'*10)
    cascade2(54321)
    print('-'*10)
    inverse_cascade(1234)
