/*
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: &#39;0&#39;, &#39;1&#39;, &#39;2&#39;, &#39;3&#39;, &#39;4&#39;, &#39;5&#39;, &#39;6&#39;, &#39;7&#39;, &#39;8&#39;, &#39;9&#39;. The wheels can rotate freely and wrap around: for example we can turn &#39;9&#39; to be &#39;0&#39;, or &#39;0&#39; to be &#39;9&#39;. Each move consists of turning one wheel one slot.

The lock initially starts at &#39;0000&#39;, a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

 
Example 1:
Input: deadends = [&quot;0201&quot;,&quot;0101&quot;,&quot;0102&quot;,&quot;1212&quot;,&quot;2002&quot;], target = &quot;0202&quot;
Output: 6
Explanation:
A sequence of valid moves would be &quot;0000&quot; -> &quot;1000&quot; -> &quot;1100&quot; -> &quot;1200&quot; -> &quot;1201&quot; -> &quot;1202&quot; -> &quot;0202&quot;.
Note that a sequence like &quot;0000&quot; -> &quot;0001&quot; -> &quot;0002&quot; -> &quot;0102&quot; -> &quot;0202&quot; would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end &quot;0102&quot;.

Example 2:
Input: deadends = [&quot;8888&quot;], target = &quot;0009&quot;
Output: 1
Explanation:
We can turn the last wheel in reverse to move from &quot;0000&quot; -> &quot;0009&quot;.

Example 3:
Input: deadends = [&quot;8887&quot;,&quot;8889&quot;,&quot;8878&quot;,&quot;8898&quot;,&quot;8788&quot;,&quot;8988&quot;,&quot;7888&quot;,&quot;9888&quot;], target = &quot;8888&quot;
Output: -1
Explanation:
We can&#39;t reach the target without getting stuck.

Example 4:
Input: deadends = [&quot;0000&quot;], target = &quot;8888&quot;
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
