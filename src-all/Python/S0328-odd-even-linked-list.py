"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL

Example 2:
Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

 
Constraints:
	The relative order inside both the even and odd groups should remain as it was in the input.
	The first node is considered odd, the second node even and so on ...
	The length of the linked list is between [0, 10^4].


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
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        pass


if __name__ == '__main__':
    assert Solution().oddEvenList(0) == 0

