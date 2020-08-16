/*
A string S of lowercase letters is given.  Then, we may make any number of moves.

In each move, we choose one of the first K letters (starting from the left), remove it, and place it at the end of the string.

Return the lexicographically smallest string we could have after any number of moves.

 

Example 1:
Input: S = &quot;cba&quot;, K = 1
Output: &quot;acb&quot;
Explanation: 
In the first move, we move the 1st character (&quot;c&quot;) to the end, obtaining the string &quot;bac&quot;.
In the second move, we move the 1st character (&quot;b&quot;) to the end, obtaining the final result &quot;acb&quot;.

Example 2:
Input: S = &quot;baaca&quot;, K = 3
Output: &quot;aaabc&quot;
Explanation: 
In the first move, we move the 1st character (&quot;b&quot;) to the end, obtaining the string &quot;aacab&quot;.
In the second move, we move the 3rd character (&quot;c&quot;) to the end, obtaining the final result &quot;aaabc&quot;.

 

Note:
	1 <= K <= S.length <= 1000
	S consists of lowercase letters only.


*/
pub struct Solution {}
impl Solution {
    pub fn orderly_queue(s: String, k: i32) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::orderly_queue(0));
  println!("Pass test cases!");
}
