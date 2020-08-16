/*
Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points symmetrically, in other words, answer whether or not if there exists a line that after reflecting all points over the given line the set of the original points is the same that the reflected ones.

Note that there can be repeated points.

Follow up:
Could you do better than O(n2) ?

 
Example 1:
Input: points = [[1,1],[-1,1]]
Output: true
Explanation: We can choose the line x = 0.

Example 2:
Input: points = [[1,1],[-1,-1]]
Output: false
Explanation: We can&#39;t choose a line.

 
Constraints:
	n == points.length
	1 <= n <= 10^4
	-10^8 <= points[i][j] <= 10^8


*/
pub struct Solution {}
impl Solution {
    pub fn is_reflected(points: Vec<Vec<i32>>) -> bool {
        
    }
}

fn main() {
  assert_eq!(0, Solution::is_reflected(0));
  println!("Pass test cases!");
}
