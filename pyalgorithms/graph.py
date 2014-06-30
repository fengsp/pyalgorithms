# -*- coding: utf-8 -*-
"""
    Graph
    ~~~~~

    Graph implementation.

    :copyright: (c) 2014 by Shipeng Feng.
    :license: BSD.
"""
import random


a, b, c, d, e, f, g, h = range(8)
N = [
    {b:2, c:1, d:3, e:9, f:4},  # a
    {c:4, e:3},                 # b
    {d:8},                      # c
    {e:7},                      # d
    {f:5},                      # e
    {c:2, g:2, h:2},            # f
    {f:1, h:6},                 # g
    {f:9, g:8}                  # h
]
_ = inf = float("inf")
W = [[0, 2, 1, 3, 9, 4, _, _], # a 
     [_, 0, 4, _, 3, _, _, _], # b 
     [_, _, 0, 8, _, _, _, _], # c 
     [_, _, _, 0, 7, _, _, _], # d 
     [_, _, _, _, 0, 5, _, _], # e 
     [_, _, 2, _, _, 0, 2, 2], # f 
     [_, _, _, _, _, 1, 0, 6], # g 
     [_, _, _, _, _, 9, 8, 0]] # h


if __name__ == "__main__":
    print b in N[a]  # Neighborhood
    print len(N[f])  # Degree
    print N[a][b]    # Edge weight for (a, b)
    print W[a][b] < inf
    print sum(1 for w in W[a] if w < inf) - 1
    print W[a][b]
    # Todo https://www.python.org/doc/essays/graphs
