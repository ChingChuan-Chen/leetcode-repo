/*
Given an array A of positive integers, A[i] represents the value of the i-th sightseeing spot, and two sightseeing spots i and j have distance j - i between them.

The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

 

Example 1:
Input: [8,1,5,2,6]
Output: 11
Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11

 

Note:
	2 <= A.length <= 50000
	1 <= A[i] <= 1000

*/
pub struct Solution {}
impl Solution {
    pub fn max_score_sightseeing_pair(a: Vec<i32>) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::max_score_sightseeing_pair(0));
  println!("Pass test cases!");
}
