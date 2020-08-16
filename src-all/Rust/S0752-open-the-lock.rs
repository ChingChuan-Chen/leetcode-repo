/*
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: &#39;0&#39;, &#39;1&#39;, &#39;2&#39;, &#39;3&#39;, &#39;4&#39;, &#39;5&#39;, &#39;6&#39;, &#39;7&#39;, &#39;8&#39;, &#39;9&#39;. The wheels can rotate freely and wrap around: for example we can turn &#39;9&#39; to be &#39;0&#39;, or &#39;0&#39; to be &#39;9&#39;. Each move consists of turning one wheel one slot.

The lock initially starts at &#39;0000&#39;, a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

 
Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".

Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".

Example 3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can&#39;t reach the target without getting stuck.

Example 4:
Input: deadends = ["0000"], target = "8888"
Output: -1

 
Constraints:
	1 <= deadends.length <= 500
	deadends[i].length == 4
	target.length == 4
	target will not be in the list deadends.
	target and deadends[i] consist of digits only.


*/
pub struct Solution {}
impl Solution {
    pub fn open_lock(deadends: Vec<String>, target: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::open_lock(0));
  println!("Pass test cases!");
}
