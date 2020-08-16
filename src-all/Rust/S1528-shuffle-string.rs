/*
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

 
Example 1:
Input: s = &quot;codeleet&quot;, indices = [4,5,6,7,0,2,1,3]
Output: &quot;leetcode&quot;
Explanation: As shown, &quot;codeleet&quot; becomes &quot;leetcode&quot; after shuffling.

Example 2:
Input: s = &quot;abc&quot;, indices = [0,1,2]
Output: &quot;abc&quot;
Explanation: After shuffling, each character remains in its position.

Example 3:
Input: s = &quot;aiohn&quot;, indices = [3,1,4,2,0]
Output: &quot;nihao&quot;

Example 4:
Input: s = &quot;aaiougrt&quot;, indices = [4,0,2,6,7,3,1,5]
Output: &quot;arigatou&quot;

Example 5:
Input: s = &quot;art&quot;, indices = [1,0,2]
Output: &quot;rat&quot;

 
Constraints:
	s.length == indices.length == n
	1 <= n <= 100
	s contains only lower-case English letters.
	0 <= indices[i] < n
	All values of indices are unique (i.e. indices is a permutation of the integers from 0 to n - 1).

*/
pub struct Solution {}
impl Solution {
    pub fn restore_string(s: String, indices: Vec<i32>) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::restore_string(0));
  println!("Pass test cases!");
}
