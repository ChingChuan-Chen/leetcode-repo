/*
Given two sparse matrices A and B, return the result of AB.

You may assume that A&#39;s column number is equal to B&#39;s row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |

 
Constraints:
	1 <= A.length, B.length <= 100
	1 <= A[i].length, B[i].length <= 100
	-100 <= A[i][j], B[i][j] <= 100


*/
pub struct Solution {}
impl Solution {
    pub fn multiply(a: Vec<Vec<i32>>, b: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::multiply(0));
  println!("Pass test cases!");
}
