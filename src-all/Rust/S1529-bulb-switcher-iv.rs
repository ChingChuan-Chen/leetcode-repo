/*
There is a room with n bulbs, numbered from 0 to n-1, arranged in a row from left to right. Initially all the bulbs are turned off.

Your task is to obtain the configuration represented by target where target[i] is &#39;1&#39; if the i-th bulb is turned on and is &#39;0&#39; if it is turned off.

You have a switch to flip the state of the bulb, a flip operation is defined as follows:

	Choose any bulb (index i) of your current configuration.
	Flip each bulb from index i to n-1.

When any bulb is flipped it means that if it is 0 it changes to 1 and if it is 1 it changes to 0.

Return the minimum number of flips required to form target.

 
Example 1:
Input: target = &quot;10111&quot;
Output: 3
Explanation: Initial configuration &quot;00000&quot;.
flip from the third bulb:  &quot;00000&quot; -> &quot;00111&quot;
flip from the first bulb:  &quot;00111&quot; -> &quot;11000&quot;
flip from the second bulb:  &quot;11000&quot; -> &quot;10111&quot;
We need at least 3 flip operations to form target.

Example 2:
Input: target = &quot;101&quot;
Output: 3
Explanation: &quot;000&quot; -> &quot;111&quot; -> &quot;100&quot; -> &quot;101&quot;.

Example 3:
Input: target = &quot;00000&quot;
Output: 0

Example 4:
Input: target = &quot;001011101&quot;
Output: 5

 
Constraints:
	1 <= target.length <= 10^5
	target[i] == &#39;0&#39; or target[i] == &#39;1&#39;


*/
pub struct Solution {}
impl Solution {
    pub fn min_flips(target: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::min_flips(0));
  println!("Pass test cases!");
}
