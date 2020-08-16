/*
Given a string path, where path[i] = &#39;N&#39;, &#39;S&#39;, &#39;E&#39; or &#39;W&#39;, each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return True if the path crosses itself at any point, that is, if at any time you are on a location you&#39;ve previously visited. Return False otherwise.

 
Example 1:
Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn&#39;t cross any point more than once.

Example 2:
Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.

 
Constraints:
	1 <= path.length <= 10^4
	path will only consist of characters in {&#39;N&#39;, &#39;S&#39;, &#39;E&#39;, &#39;W}


*/
pub struct Solution {}
impl Solution {
    pub fn is_path_crossing(path: String) -> bool {
        
    }
}

fn main() {
  assert_eq!(0, Solution::is_path_crossing(0));
  println!("Pass test cases!");
}
