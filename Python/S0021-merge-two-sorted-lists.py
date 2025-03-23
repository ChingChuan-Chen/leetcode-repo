"""
Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import List


def from_list(vals: List[int]) -> ListNode:
    current = None
    for x in vals[::-1]:
        current = ListNode(x, current)
    return current


def to_list(list_node: ListNode) -> List[int]:
    vals = []
    while list_node is not None:
        vals.append(list_node.val)
        list_node = list_node.next
    return vals


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # List 1 is empty, then result is decided by List 2
        if not l1:
            return l2

        # List 2 is empty, then result is decided by List 1
        if not l2:
            return l1

        # General cases: compare node value, and update linkage
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1

        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':
    ex1 = Solution().mergeTwoLists(from_list([1, 2, 4]), from_list([1, 3, 4]))
    assert to_list(ex1) == [1, 1, 2, 3, 4, 4]
    ex2 = Solution().mergeTwoLists(from_list([1, 4, 5]), from_list([1, 3, 4]))
    assert to_list(ex2) == [1, 1, 3, 4, 4, 5]
