"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
 Input: 1->1->2
 Output: 1->2

Example 2:
 Input: 1->1->2->3->3
 Output: 1->2->3
"""

# Definition for singly-linked list.
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        if cur is None or cur.next is None:
            return head
        next_node = cur.next
        while cur is not None and next_node is not None:
            if cur.val == next_node.val:
                next_node = next_node.next
            else:
                cur.next = next_node
                cur = cur.next
                next_node = cur.next
        cur.next = None
        return head

if __name__ == '__main__':
    assert to_list(Solution().deleteDuplicates(from_list([1, 1, 2]))) == [1, 2]
    assert to_list(Solution().deleteDuplicates(from_list([1, 1, 2, 3, 3]))) == [1, 2, 3]
    assert to_list(Solution().deleteDuplicates(from_list([1, 1, 1, 2, 3, 3, 3]))) == [1, 2, 3]
    assert to_list(Solution().deleteDuplicates(from_list([1]))) == [1]
    assert to_list(Solution().deleteDuplicates(from_list([]))) == []
