#!/usr/bin/env python
# coding: utf-8

if __name__ == '__main__':
    """
    [] arasında olduğunda tüm listenin içeriğini
    hafızada tutar.
    """
    my_list = [x * x for x in range(3)]
    
    for i in my_list:
        print i

    print '--- %d ' % len(my_list)

    """
    () arasındayken sadece gerektiğinde(on-the-fly)
    yaratılır, işi bittikten sonra hafızadan silinir.
    """
    my_generator = (x * x for x in range(3))

    for i in my_generator:
        print i

    print '--- %d' % sum(my_generator)
