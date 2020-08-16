/*
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

	direction can be 0 (for left shift) or 1 (for right shift). 
	amount is the amount by which string s is to be shifted.
	A left shift by 1 means remove the first character of s and append it to the end.
	Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.

Return the final string after all operations.

 
Example 1:
Input: s = &quot;abc&quot;, shift = [[0,1],[1,2]]
Output: &quot;cab&quot;
Explanation: 
[0,1] means shift to left by 1. &quot;abc&quot; -> &quot;bca&quot;
[1,2] means shift to right by 2. &quot;bca&quot; -> &quot;cab&quot;

Example 2:
Input: s = &quot;abcdefg&quot;, shift = [[1,1],[1,1],[0,2],[1,3]]
Output: &quot;efgabcd&quot;
Explanation:  
[1,1] means shift to right by 1. &quot;abcdefg&quot; -> &quot;gabcdef&quot;
[1,1] means shift to right by 1. &quot;gabcdef&quot; -> &quot;fgabcde&quot;
[0,2] means shift to left by 2. &quot;fgabcde&quot; -> &quot;abcdefg&quot;
[1,3] means shift to right by 3. &quot;abcdefg&quot; -> &quot;efgabcd&quot;

 
Constraints:
	1 <= s.length <= 100
	s only contains lower case English letters.
	1 <= shift.length <= 100
	shift[i].length == 2
	0 <= shift[i][0] <= 1
	0 <= shift[i][1] <= 100

*/
pub struct Solution {}
impl Solution {
    pub fn string_shift(s: String, shift: Vec<Vec<i32>>) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::string_shift(0));
  println!("Pass test cases!");
}
