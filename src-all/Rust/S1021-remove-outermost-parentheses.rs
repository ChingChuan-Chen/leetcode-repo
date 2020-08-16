/*
A valid parentheses string is either empty (&quot;&quot;), &quot;(&quot; + A + &quot;)&quot;, or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, &quot;&quot;, &quot;()&quot;, &quot;(())()&quot;, and &quot;(()(()))&quot; are all valid parentheses strings.

A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

 

Example 1:
Input: &quot;(()())(())&quot;
Output: &quot;()()()&quot;
Explanation: 
The input string is &quot;(()())(())&quot;, with primitive decomposition &quot;(()())&quot; + &quot;(())&quot;.
After removing outer parentheses of each part, this is &quot;()()&quot; + &quot;()&quot; = &quot;()()()&quot;.

Example 2:
Input: &quot;(()())(())(()(()))&quot;
Output: &quot;()()()()(())&quot;
Explanation: 
The input string is &quot;(()())(())(()(()))&quot;, with primitive decomposition &quot;(()())&quot; + &quot;(())&quot; + &quot;(()(()))&quot;.
After removing outer parentheses of each part, this is &quot;()()&quot; + &quot;()&quot; + &quot;()(())&quot; = &quot;()()()()(())&quot;.

Example 3:
Input: &quot;()()&quot;
Output: &quot;&quot;
Explanation: 
The input string is &quot;()()&quot;, with primitive decomposition &quot;()&quot; + &quot;()&quot;.
After removing outer parentheses of each part, this is &quot;&quot; + &quot;&quot; = &quot;&quot;.

 

Note:
	S.length <= 10000
	S[i] is &quot;(&quot; or &quot;)&quot;
	S is a valid parentheses string

 


*/
pub struct Solution {}
impl Solution {
    pub fn remove_outer_parentheses(s: String) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::remove_outer_parentheses(0));
  println!("Pass test cases!");
}
