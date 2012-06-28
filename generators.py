#!/usr/bin/env python
# coding: utf-8


def main():
    # Tüm listenin içeriğini hafızada tutar.
    my_list = [x * x for x in range(3)]

    # Sadece gerektiğinde(on-the-fly) yaratılır,
    # işi bittikten sonra hafızadan silinir.
    my_generator = (x * x for x in range(3))

    print '{0:d} - {1:d}'.format(sum(my_list), sum(my_generator))

if __name__ == '__main__':
    main()
