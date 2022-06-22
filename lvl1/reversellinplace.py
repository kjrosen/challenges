"""Given linked list, reverse the nodes in this linked list in place.

Iterative solution doctest:
    
    >>> ll1 = LinkedList(Node(1, Node(2, Node(3))))
    >>> ll1.as_string()
    '123'
    >>> reverse_linked_list_in_place(ll1)
    >>> ll1.as_string()
    '321'

Recursive solution doctest:

    >>> ll2 = LinkedList(Node(1, Node(2, Node(3))))
    >>> ll2.as_string()
    '123'
    >>> reverse_linked_list_in_place_rec(ll2)
    >>> ll2.as_string()
    '321'
"""


from flask import current_app


class LinkedList(object):
    """Linked list."""

    def __init__(self, head=None):
        self.head = head

    def as_string(self):
        """Represent data for this list as a string.

        >>> LinkedList(Node(3)).as_string()
        '3'

        >>> LinkedList(Node(3, Node(2, Node(1)))).as_string()
        '321'
        """

        out = []
        n = self.head

        while n:
            out.append(str(n.data))
            n = n.next

        return "".join(out)


class Node(object):
    """Class in a linked list."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Iteration solution.
def reverse_linked_list_in_place(lst):
    """Given linked list, reverse the nodes in this linked list in place."""

    current, prev, next = lst.head, None, lst.head.next

    while next:
        current.next = prev

        prev = current
        current = next
        next = current.next

    current.next = prev
    lst.head = current


def reverse_linked_list_in_place_rec(lst):
    """reverses a linked list in place using recursion"""

    prev, curr = None, lst.head
    
    def _reverse(curr, prev):

        ## if current node == none, return previous node
        if not curr:
            return prev

        ## save next, then set current next to previous
        nxt = curr.next
        curr.next = prev
        ## move to next node
        prev = curr
        curr = nxt

        ## repeat on next set of nodes
        return _reverse(curr, prev)

    lst.head = _reverse(curr, prev)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. RIGHT ON!\n")
