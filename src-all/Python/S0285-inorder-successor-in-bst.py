"""
Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

The successor of a node p is the node with the smallest key greater than p.val.

 

Example 1:
Input: root = [2,1,3], p = 1
Output: 2
Explanation: 1&#39;s in-order successor node is 2. Note that both p and the return value is of TreeNode type.

Example 2:
Input: root = [5,3,6,2,4,null,null,1], p = 6
Output: null
Explanation: There is no in-order successor of the current node, so the answer is null.

 

Note:
	If the given node has no in-order successor in the tree, return null.
	It&#39;s guaranteed that the values of the tree are unique.


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        
        pass


if __name__ == '__main__':
    assert Solution().inorderSuccessor(0) == 0

