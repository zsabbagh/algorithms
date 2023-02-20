"""
A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""
from collections import defaultdict
import unittest

class RandomListNode(object):
    def __init__(self, label):
        self.label = label
        self.next = None
        self.random = None


def copy_random_pointer_v1(head):
    """
    :type head: RandomListNode
    :rtype: RandomListNode
    """
    dic = dict()
    m = n = head
    while m:
        dic[m] = RandomListNode(m.label)
        m = m.next
    while n:
        dic[n].next = dic.get(n.next)
        dic[n].random = dic.get(n.random)
        n = n.next
    return dic.get(head)


# O(n)
def copy_random_pointer_v2(head):
    """
    :type head: RandomListNode
    :rtype: RandomListNode
    """
    copy = defaultdict(lambda: RandomListNode(0))
    copy[None] = None
    node = head
    while node:
        copy[node].label = node.label
        copy[node].next = copy[node.next]
        copy[node].random = copy[node.random]
        node = node.next
    return copy[head]


class TestCopyRandomPointer(unittest.TestCase):
    def test_copy_random_pointer(self):
        node1 = RandomListNode(1)
        node2 = RandomListNode(2)
        node3 = RandomListNode(3)
        node4 = RandomListNode(4)
        node5 = RandomListNode(5)

        node1.next = node2
        node1.random = node3

        node2.next = node3
        node2.random = node1

        node3.next = node4
        node3.random = node3

        node4.next = node5
        node4.random = node2

        node5.random = node4

        new_head = copy_random_pointer_v2(node1)

        # Check that the original and new linked lists are not the same
        self.assertIsNot(node1, new_head)

        # Check that the nodes have the same values
        self.assertEqual(node1.label, new_head.label)
        self.assertEqual(node2.label, new_head.next.label)
        self.assertEqual(node3.label, new_head.next.next.label)
        self.assertEqual(node4.label, new_head.next.next.next.label)
        self.assertEqual(node5.label, new_head.next.next.next.next.label)

        # Check that the nodes are not the same objects
        self.assertIsNot(node1, new_head)
        self.assertIsNot(node2, new_head.next)
        self.assertIsNot(node3, new_head.next.next)
        self.assertIsNot(node4, new_head.next.next.next)
        self.assertIsNot(node5, new_head.next.next.next.next)

        # Check that the random pointers were copied correctly
        self.assertIs(new_head.next.next, new_head.random)
        self.assertIs(new_head.next.next.next.next, new_head.next.random)
        self.assertIs(new_head, new_head.next.random)
        self.assertIs(new_head.next.next, new_head.next.next.random)
        self.assertIs(new_head.next.next.next, new_head.next.random)

        if __name__ == '__main__':

            unittest.main()
