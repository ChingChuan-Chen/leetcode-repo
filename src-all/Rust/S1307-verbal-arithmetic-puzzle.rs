/*
Given an equation, represented by words on left side and the result on right side.

You need to check if the equation is solvable under the following rules:

	Each character is decoded as one digit (0 - 9).
	Every pair of different characters they must map to different digits.
	Each words[i] and result are decoded as one number without leading zeros.
	Sum of numbers on left side (words) will equal to the number on right side (result). 

Return True if the equation is solvable otherwise return False.

 
Example 1:
Input: words = [&quot;SEND&quot;,&quot;MORE&quot;], result = &quot;MONEY&quot;
Output: true
Explanation: Map &#39;S&#39;-> 9, &#39;E&#39;->5, &#39;N&#39;->6, &#39;D&#39;->7, &#39;M&#39;->1, &#39;O&#39;->0, &#39;R&#39;->8, &#39;Y&#39;->&#39;2&#39;
Such that: &quot;SEND&quot; + &quot;MORE&quot; = &quot;MONEY&quot; ,  9567 + 1085 = 10652

Example 2:
Input: words = [&quot;SIX&quot;,&quot;SEVEN&quot;,&quot;SEVEN&quot;], result = &quot;TWENTY&quot;
Output: true
Explanation: Map &#39;S&#39;-> 6, &#39;I&#39;->5, &#39;X&#39;->0, &#39;E&#39;->8, &#39;V&#39;->7, &#39;N&#39;->2, &#39;T&#39;->1, &#39;W&#39;->&#39;3&#39;, &#39;Y&#39;->4
Such that: &quot;SIX&quot; + &quot;SEVEN&quot; + &quot;SEVEN&quot; = &quot;TWENTY&quot; ,  650 + 68782 + 68782 = 138214

Example 3:
Input: words = [&quot;THIS&quot;,&quot;IS&quot;,&quot;TOO&quot;], result = &quot;FUNNY&quot;
Output: true

Example 4:
Input: words = [&quot;LEET&quot;,&quot;CODE&quot;], result = &quot;POINT&quot;
Output: false

 
Constraints:
	2 <= words.length <= 5
	1 <= words[i].length, result.length <= 7
	words[i], result contains only upper case English letters.
	Number of different characters used on the expression is at most 10.


*/
pub struct Solution {}
impl Solution {
    pub fn is_solvable(words: Vec<String>, result: String) -> bool {
        
    }
}

fn main() {
  assert_eq!(0, Solution::is_solvable(0));
  println!("Pass test cases!");
}
