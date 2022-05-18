/*
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

 
Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []

 
Constraints:
	The number of nodes in the list is in the range [0, 104].
	1 <= Node.val <= 50
	0 <= val <= 50


*/

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

#include <cassert>
#include <iostream>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.ListNode(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
