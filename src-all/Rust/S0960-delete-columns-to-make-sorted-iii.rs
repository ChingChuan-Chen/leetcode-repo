/*
We are given an array A of N lowercase letter strings, all of the same length.

Now, we may choose any set of deletion indices, and for each string, we delete all the characters in those indices.

For example, if we have an array A = [&quot;babca&quot;,&quot;bbazb&quot;] and deletion indices {0, 1, 4}, then the final array after deletions is [&quot;bc&quot;,&quot;az&quot;].

Suppose we chose a set of deletion indices D such that after deletions, the final array has every element (row) in lexicographic order.

For clarity, A[0] is in lexicographic order (ie. A[0][0] <= A[0][1] <= ... <= A[0][A[0].length - 1]), A[1] is in lexicographic order (ie. A[1][0] <= A[1][1] <= ... <= A[1][A[1].length - 1]), and so on.

Return the minimum possible value of D.length.

 

Example 1:
Input: [&quot;babca&quot;,&quot;bbazb&quot;]
Output: 3
Explanation: After deleting columns 0, 1, and 4, the final array is A = [&quot;bc&quot;, &quot;az&quot;].
Both these rows are individually in lexicographic order (ie. A[0][0] <= A[0][1] and A[1][0] <= A[1][1]).
Note that A[0] > A[1] - the array A isn&#39;t necessarily in lexicographic order.

Example 2:
Input: [&quot;edcba&quot;]
Output: 4
Explanation: If we delete less than 4 columns, the only row won&#39;t be lexicographically sorted.

Example 3:
Input: [&quot;ghi&quot;,&quot;def&quot;,&quot;abc&quot;]
Output: 0
Explanation: All rows are already lexicographically sorted.

 

Note:
	1 <= A.length <= 100
	1 <= A[i].length <= 100

*/
pub struct Solution {}
impl Solution {
    pub fn min_deletion_size(a: Vec<String>) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::min_deletion_size(0));
  println!("Pass test cases!");
}
