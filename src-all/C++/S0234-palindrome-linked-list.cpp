/*
Given the head of a singly linked list, return true if it is a palindrome.

 
Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

 
Constraints:
	The number of nodes in the list is in the range [1, 105].
	0 <= Node.val <= 9

 
Follow up: Could you do it in O(n) time and O(1) space?
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
    bool isPalindrome(ListNode* head) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.ListNode(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
