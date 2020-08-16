/*
You are given a tree with n nodes numbered from 0 to n-1 in the form of a parent array where parent[i] is the parent of node i. The root of the tree is node 0.

Implement the function getKthAncestor(int node, int k) to return the k-th ancestor of the given node. If there is no such ancestor, return -1.

The k-th ancestor of a tree node is the k-th node in the path from that node to the root.

 

Example:

Input:
[&quot;TreeAncestor&quot;,&quot;getKthAncestor&quot;,&quot;getKthAncestor&quot;,&quot;getKthAncestor&quot;]
[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]

Output:
[null,1,0,-1]

Explanation:
TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);

treeAncestor.getKthAncestor(3, 1);  // returns 1 which is the parent of 3
treeAncestor.getKthAncestor(5, 2);  // returns 0 which is the grandparent of 5
treeAncestor.getKthAncestor(6, 3);  // returns -1 because there is no such ancestor

 
Constraints:
	1 <= k <= n <= 5*10^4
	parent[0] == -1 indicating that 0 is the root node.
	0 <= parent[i] < n for all 0 < i < n
	0 <= node < n
	There will be at most 5*10^4 queries.

*/
pub struct Solution {}
struct TreeAncestor {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl TreeAncestor {

    fn new(n: i32, parent: Vec<i32>) -> Self {
        
    }
    
    fn get_kth_ancestor(&self, node: i32, k: i32) -> i32 {
        
    }
}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * let obj = TreeAncestor::new(n, parent);
 * let ret_1: i32 = obj.get_kth_ancestor(node, k);
 */

fn main() {
  assert_eq!(0, Solution::new(0));
  println!("Pass test cases!");
}
