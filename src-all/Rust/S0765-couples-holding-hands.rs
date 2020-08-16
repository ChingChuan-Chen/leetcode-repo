/*

N couples sit in 2N seats arranged in a row and want to hold hands.  We want to know the minimum number of swaps so that every couple is sitting side by side.  A swap consists of choosing any two people, then they stand up and switch seats. 

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.

Example 1:
Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.

Example 2:
Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.

Note:
 
 len(row) is even and in the range of [4, 60].
 row is guaranteed to be a permutation of 0...len(row)-1.

*/
pub struct Solution {}
impl Solution {
    pub fn min_swaps_couples(row: Vec<i32>) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::min_swaps_couples(0));
  println!("Pass test cases!");
}
