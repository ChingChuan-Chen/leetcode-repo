"""
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

 

Example:

BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false

 

Note:
	next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
	You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.


"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        

    def next(self) -> int:
        """
        @return the next smallest number
        """
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        


# param_2 = obj.hasNext()
        pass


if __name__ == '__main__':
    assert Solution().__init__(0) == 0

