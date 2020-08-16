"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 <= m <= n <= length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL


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
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        pass


if __name__ == '__main__':
    assert Solution().reverseBetween(0) == 0

