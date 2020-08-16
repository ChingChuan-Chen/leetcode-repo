/*
Given a string s. You should re-order the string using the following algorithm:

	Pick the smallest character from s and append it to the result.
	Pick the smallest character from s which is greater than the last appended character to the result and append it.
	Repeat step 2 until you cannot pick more characters.
	Pick the largest character from s and append it to the result.
	Pick the largest character from s which is smaller than the last appended character to the result and append it.
	Repeat step 5 until you cannot pick more characters.
	Repeat the steps from 1 to 6 until you pick all characters from s.

In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.

Return the result string after sorting s with this algorithm.

 
Example 1:
Input: s = &quot;aaaabbbbcccc&quot;
Output: &quot;abccbaabccba&quot;
Explanation: After steps 1, 2 and 3 of the first iteration, result = &quot;abc&quot;
After steps 4, 5 and 6 of the first iteration, result = &quot;abccba&quot;
First iteration is done. Now s = &quot;aabbcc&quot; and we go back to step 1
After steps 1, 2 and 3 of the second iteration, result = &quot;abccbaabc&quot;
After steps 4, 5 and 6 of the second iteration, result = &quot;abccbaabccba&quot;

Example 2:
Input: s = &quot;rat&quot;
Output: &quot;art&quot;
Explanation: The word &quot;rat&quot; becomes &quot;art&quot; after re-ordering it with the mentioned algorithm.

Example 3:
Input: s = &quot;leetcode&quot;
Output: &quot;cdelotee&quot;

Example 4:
Input: s = &quot;ggggggg&quot;
Output: &quot;ggggggg&quot;

Example 5:
Input: s = &quot;spo&quot;
Output: &quot;ops&quot;

 
Constraints:
	1 <= s.length <= 500
	s contains only lower-case English letters.


*/
pub struct Solution {}
impl Solution {
    pub fn sort_string(s: String) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::sort_string(0));
  println!("Pass test cases!");
}
