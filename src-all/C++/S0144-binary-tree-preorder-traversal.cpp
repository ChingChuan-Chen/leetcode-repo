/*
Given the root of a binary tree, return the preorder traversal of its nodes' values.

 
Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

 
Constraints:
	The number of nodes in the tree is in the range [0, 100].
	-100 <= Node.val <= 100

 
Follow up: Recursive solution is trivial, could you do it iteratively?

*/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#include <cassert>
#include <iostream>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        
    }
};

int main() {
  Solution sol;
  assert(sol.TreeNode(0) == 0);
  std::cout << "Pass test cases!" << std::endl;
}
