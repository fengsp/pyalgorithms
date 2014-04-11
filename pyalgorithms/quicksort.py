# -*- coding: utf-8 -*-
"""
    QuickSort
    ~~~~~~~~~

    One elegant quicksort implementation.

    :copyright: (c) 2013 by fsp.
    :license: BSD.
"""
import random


def swap(array, x, y):
    array[x], array[y] = array[y], array[x]


def quicksort(array, l, r):
    if l >= r: return
    # find a flag and make lefts smaller than flag
    m = random.randint(l, r)
    swap(array, l, m)
    m = l
    for i in range(l+1, r+1):
        if array[i] < array[l]:
            m += 1
            swap(array, m, i)
    swap(array, m, l)
    quicksort(array, l, m-1)
    quicksort(array, m+1, r)


if __name__ == "__main__":
    l = [5, 7, 0, 4, 3, 90, 56, 34]
    print l
    quicksort(l, 0, len(l)-1)
    print l
