/*
An image is represented by a binary matrix with 0 as a white pixel and 1 as a black pixel. The black pixels are connected, i.e., there is only one black region. Pixels are connected horizontally and vertically. Given the location (x, y) of one of the black pixels, return the area of the smallest (axis-aligned) rectangle that encloses all black pixels.

Example:

Input:
[
  "0010",
  "0110",
  "0100"
]
and x = 0, y = 2

Output: 6


*/
pub struct Solution {}
impl Solution {
    pub fn min_area(image: Vec<Vec<char>>, x: i32, y: i32) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::min_area(0));
  println!("Pass test cases!");
}
