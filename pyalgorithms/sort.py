# -*- coding: utf-8 -*-
"""
    Sort
    ~~~~

    Sorting implementation.

    :copyright: (c) 2013 by fsp.
    :license: BSD.
"""
import random


def swap(seq, x, y):
    seq[x], seq[y] = seq[y], seq[x]


def quicksort(seq, l, r):
    if l >= r: return
    # find a flag and make lefts smaller than flag
    m = random.randint(l, r)
    swap(seq, l, m)
    m = l
    for i in range(l+1, r+1):
        if seq[i] < seq[l]:
            m += 1
            swap(seq, m, i)
    swap(seq, m, l)
    quicksort(seq, l, m-1)
    quicksort(seq, m+1, r)


def gnomesort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            swap(seq, i, i-1)
            i -= 1


def mergesort(seq):
    if len(seq) < 2:
        return seq
    mid = len(seq) / 2
    left, right = seq[:mid], seq[mid:]
    left = mergesort(left)
    right = mergesort(right)
    result = []
    while left and right:
        if left[-1] >= right[-1]:
            result.append(left.pop())
        else:
            result.append(right.pop())
    result.reverse()
    return (left or right) + result


if __name__ == "__main__":
    l = [5, 7, 0, 4, 3, 90, 56, 34]
    print l
    quicksort(l, 0, len(l)-1)
    print l
    l = [5, 7, 0, 4, 3, 90, 56, 34]
    gnomesort(l)
    print l
    l = [5, 7, 0, 4, 3, 90, 56, 34]
    print mergesort(l)
