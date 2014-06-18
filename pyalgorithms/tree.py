# -*- coding: utf-8 -*-
"""
    Tree
    ~~~~

    Tree implementation.

    :copyright: (c) 2014 by fsp.
    :license: BSD.
"""

class BinaryTree(object):
    """A Binary Tree Class.

    :param value: val
    :param left: left child
    :param right: right child
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class MultiwayTree(object):
    """A Multiway Tree Class.

    :param value: val
    :param child: first child
    :param next: next sibling
    """

    def __init__(self, value, child=None, next=None):
        self.value = value
        self.child = child
        self.next = next

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


if __name__ == "__main__":
    binary_tree = BinaryTree("root", BinaryTree("a", BinaryTree("c")),
                             BinaryTree("b", right=BinaryTree("d")))
    print binary_tree
    print binary_tree.left.left
    print binary_tree.right.right

    multiway_tree = MultiwayTree("root", MultiwayTree("a",
                                 next=MultiwayTree("b", MultiwayTree("c"))))
    print multiway_tree
    print multiway_tree.child.next.child
