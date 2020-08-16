/*
Let&#39;s say a positive integer is a superpalindrome if it is a palindrome, and it is also the square of a palindrome.

Now, given two positive integers L and R (represented as strings), return the number of superpalindromes in the inclusive range [L, R].

 

Example 1:
Input: L = &quot;4&quot;, R = &quot;1000&quot;
Output: 4
Explanation: 4, 9, 121, and 484 are superpalindromes.
Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.

 

Note:
	1 <= len(L) <= 18
	1 <= len(R) <= 18
	L and R are strings representing integers in the range [1, 10^18).
	int(L) <= int(R)

 


*/
pub struct Solution {}
impl Solution {
    pub fn superpalindromes_in_range(l: String, r: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::superpalindromes_in_range(0));
  println!("Pass test cases!");
}
