/*
Given an array of citations sorted in ascending order (each citation is a non-negative integer) of a researcher, write a function to compute the researcher&#39;s h-index.

According to the definition of h-index on Wikipedia: &quot;A scientist has index h if h of his/her N papers have at least h citations each, and the other N &minus; h papers have no more than h citations each.&quot;

Example:

Input: citations = [0,1,3,5,6]
Output: 3 
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them had 
             received 0, 1, 3, 5, 6 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.

Note:
If there are several possible values for h, the maximum one is taken as the h-index.

Follow up:
	This is a follow up problem to H-Index, where citations is now guaranteed to be sorted in ascending order.
	Could you solve it in logarithmic time complexity?


*/
pub struct Solution {}
impl Solution {
    pub fn h_index(citations: Vec<i32>) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::h_index(0));
  println!("Pass test cases!");
}
