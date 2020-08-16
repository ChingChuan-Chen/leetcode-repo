/*
In a string S of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like S = &quot;abbxxxxzyy&quot; has the groups &quot;a&quot;, &quot;bb&quot;, &quot;xxxx&quot;, &quot;z&quot; and &quot;yy&quot;.

Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.

The final answer should be in lexicographic order.

 

Example 1:
Input: &quot;abbxxxxzzy&quot;
Output: [[3,6]]
Explanation: &quot;xxxx&quot; is the single large group with starting  3 and ending positions 6.

Example 2:
Input: &quot;abc&quot;
Output: []
Explanation: We have &quot;a&quot;,&quot;b&quot; and &quot;c&quot; but no large group.

Example 3:
Input: &quot;abcdddeeeeaabbbcd&quot;
Output: [[3,5],[6,9],[12,14]]

 

Note:  1 <= S.length <= 1000

*/
pub struct Solution {}
impl Solution {
    pub fn large_group_positions(s: String) -> Vec<Vec<i32>> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::large_group_positions(0));
  println!("Pass test cases!");
}
