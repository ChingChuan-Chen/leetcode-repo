/*
A decimal number can be converted to its Hexspeak representation by first converting it to an uppercase hexadecimal string, then replacing all occurrences of the digit 0 with the letter O, and the digit 1 with the letter I.  Such a representation is valid if and only if it consists only of the letters in the set {&quot;A&quot;, &quot;B&quot;, &quot;C&quot;, &quot;D&quot;, &quot;E&quot;, &quot;F&quot;, &quot;I&quot;, &quot;O&quot;}.

Given a string num representing a decimal integer N, return the Hexspeak representation of N if it is valid, otherwise return &quot;ERROR&quot;.

 
Example 1:
Input: num = &quot;257&quot;
Output: &quot;IOI&quot;
Explanation:  257 is 101 in hexadecimal.

Example 2:
Input: num = &quot;3&quot;
Output: &quot;ERROR&quot;

 
Constraints:
	1 <= N <= 10^12
	There are no leading zeros in the given string.
	All answers must be in uppercase letters.


*/
pub struct Solution {}
impl Solution {
    pub fn to_hexspeak(num: String) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::to_hexspeak(0));
  println!("Pass test cases!");
}
