/*
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive &quot;++&quot; into &quot;--&quot;. The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

Example:

Input: s = &quot;++++&quot;
Output: 
[
  &quot;--++&quot;,
  &quot;+--+&quot;,
  &quot;++--&quot;
]

Note: If there is no valid move, return an empty list [].

*/
pub struct Solution {}
impl Solution {
    pub fn generate_possible_next_moves(s: String) -> Vec<String> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::generate_possible_next_moves(0));
  println!("Pass test cases!");
}
