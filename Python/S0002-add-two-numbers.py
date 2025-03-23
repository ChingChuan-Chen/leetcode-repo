"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        current = dummy_head
        overflow = False
        while l1 or l2 or overflow:
            node_val = 1 if overflow else 0
            node_val += l1.val if l1 else 0
            node_val += l2.val if l2 else 0
            overflow = True if node_val >= 10 else False
            node_val -= 10 if overflow else 0
            current.next = ListNode(node_val)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy_head.next


if __name__ == '__main__':
    assert to_list(Solution().addTwoNumbers(from_list([2, 4, 3]), from_list([5, 6, 4]))) == [7, 0, 8]
    assert to_list(Solution().addTwoNumbers(from_list([3, 4]), from_list([4, 6]))) == [7, 0, 1]
    assert to_list(Solution().addTwoNumbers(from_list([9, 9, 9, 9]), from_list([9, 9, 9, 9, 9, 9]))) == [8, 9, 9, 9, 0, 0, 1]
    assert to_list(Solution().addTwoNumbers(from_list([0]), from_list([0]))) == [0]
