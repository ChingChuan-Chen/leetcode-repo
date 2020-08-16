/*
Let&#39;s define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = &quot;dcce&quot; then f(s) = 2 because the smallest character is &quot;c&quot; and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

 
Example 1:
Input: queries = [&quot;cbd&quot;], words = [&quot;zaaaz&quot;]
Output: [1]
Explanation: On the first query we have f(&quot;cbd&quot;) = 1, f(&quot;zaaaz&quot;) = 3 so f(&quot;cbd&quot;) < f(&quot;zaaaz&quot;).

Example 2:
Input: queries = [&quot;bbb&quot;,&quot;cc&quot;], words = [&quot;a&quot;,&quot;aa&quot;,&quot;aaa&quot;,&quot;aaaa&quot;]
Output: [1,2]
Explanation: On the first query only f(&quot;bbb&quot;) < f(&quot;aaaa&quot;). On the second query both f(&quot;aaa&quot;) and f(&quot;aaaa&quot;) are both > f(&quot;cc&quot;).

 
Constraints:
	1 <= queries.length <= 2000
	1 <= words.length <= 2000
	1 <= queries[i].length, words[i].length <= 10
	queries[i][j], words[i][j] are English lowercase letters.


*/
pub struct Solution {}
impl Solution {
    pub fn num_smaller_by_frequency(queries: Vec<String>, words: Vec<String>) -> Vec<i32> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::num_smaller_by_frequency(0));
  println!("Pass test cases!");
}
