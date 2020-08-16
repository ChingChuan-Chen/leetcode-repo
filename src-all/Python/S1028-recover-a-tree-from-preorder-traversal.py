"""
We run a preorder depth first search on the root of a binary tree.

At each node in this traversal, we output D dashes (where D is the depth of this node), then we output the value of this node.  (If the depth of a node is D, the depth of its immediate child is D+1.  The depth of the root node is 0.)

If a node has only one child, that child is guaranteed to be the left child.

Given the output S of this traversal, recover the tree and return its root.

 

Example 1:
Input: &quot;1-2--3--4-5--6--7&quot;
Output: [1,2,5,3,4,6,7]

Example 2:
Input: &quot;1-2--3---4-5--6---7&quot;
Output: [1,2,5,3,null,6,null,4,null,7]

 

Example 3:
Input: &quot;1-401--349---90--88&quot;
Output: [1,401,null,349,88,90]

 

Note:
	The number of nodes in the original tree is between 1 and 1000.
	Each node will have a value between 1 and 10^9.


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        
        pass


if __name__ == '__main__':
    assert Solution().recoverFromPreorder(0) == 0

