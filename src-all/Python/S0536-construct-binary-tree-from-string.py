"""
You need to construct a binary tree from a string consisting of parenthesis and integers. 

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure. 

You always start to construct the left child node of the parent first if it exists.

Example:

Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   / 
  3   1 5   

Note:
There will only be '(',  ')',  '-' and  '0' ~ '9' in the input string.
An empty tree is represented by "" instead of "()".

 
Constraints: 
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        
        pass


if __name__ == '__main__':
    assert Solution().str2tree(0) == 0

