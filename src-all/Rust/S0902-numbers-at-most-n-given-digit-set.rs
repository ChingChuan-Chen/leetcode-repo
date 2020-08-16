/*
We have a sorted set of digits D, a non-empty subset of {&#39;1&#39;,&#39;2&#39;,&#39;3&#39;,&#39;4&#39;,&#39;5&#39;,&#39;6&#39;,&#39;7&#39;,&#39;8&#39;,&#39;9&#39;}.  (Note that &#39;0&#39; is not included.)

Now, we write numbers using these digits, using each digit as many times as we want.  For example, if D = {&#39;1&#39;,&#39;3&#39;,&#39;5&#39;}, we may write numbers such as &#39;13&#39;, &#39;551&#39;, &#39;1351315&#39;.

Return the number of positive integers that can be written (using the digits of D) that are less than or equal to N.

 

Example 1:
Input: D = ["1","3","5","7"], N = 100
Output: 20
Explanation: 
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.

Example 2:
Input: D = ["1","4","9"], N = 1000000000
Output: 29523
Explanation: 
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits of D.

 

Note:
	D is a subset of digits &#39;1&#39;-&#39;9&#39; in sorted order.
	1 <= N <= 10^9


*/
pub struct Solution {}
impl Solution {
    pub fn at_most_n_given_digit_set(d: Vec<String>, n: i32) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::at_most_n_given_digit_set(0));
  println!("Pass test cases!");
}
