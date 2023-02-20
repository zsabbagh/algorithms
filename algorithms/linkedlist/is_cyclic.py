"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
"""
class Node:

    def __init__(self, x):
        self.val = x
        self.next = None

def is_cyclic(head):
    """
    :type head: Node
    :rtype: bool
    """
    if not head:
        return False
    runner = head
    walker = head
    while runner.next and runner.next.next:
        runner = runner.next.next
        walker = walker.next
        if runner == walker:
            return True
    return False

import unittest

class TestLinkedListCycle(unittest.TestCase):

    def test_is_cyclic(self):

        # create a cyclic linked list 1 -> 2 -> 3 -> 4 -> 2
        head = Node(1)
        curr = head
        for i in range(2, 5):
            curr.next = Node(i)
            curr = curr.next
        curr.next = head.next

        self.assertTrue(is_cyclic(head))

        # create a non-cyclic linked list 1 -> 2 -> 3 -> 4 -> None
        head = Node(1)
        curr = head
        for i in range(2, 5):
            curr.next = Node(i)
            curr = curr.next

        self.assertFalse(is_cyclic(head))

        # test an empty list
        self.assertFalse(is_cyclic(None))
