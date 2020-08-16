/*
We are stacking blocks to form a pyramid. Each block has a color which is a one letter string.

We are allowed to place any color block C on top of two adjacent blocks of colors A and B, if and only if ABC is an allowed triple.

We start with a bottom row of bottom, represented as a single string. We also start with a list of allowed triples allowed. Each allowed triple is represented as a string of length 3.

Return true if we can build the pyramid all the way to the top, otherwise false.

Example 1:
Input: bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
Output: true
Explanation:
We can stack the pyramid like this:
    A
   / \
  G   E
 / \ / \
B   C   D

We are allowed to place G on top of B and C because BCG is an allowed triple.  Similarly, we can place E on top of C and D, then A on top of G and E.

 

Example 2:
Input: bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
Output: false
Explanation:
We can&#39;t stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.

 
Constraints:
	bottom will be a string with length in range [2, 8].
	allowed will have length in range [0, 200].
	Letters in all strings will be chosen from the set {&#39;A&#39;, &#39;B&#39;, &#39;C&#39;, &#39;D&#39;, &#39;E&#39;, &#39;F&#39;, &#39;G&#39;}.


*/
pub struct Solution {}
impl Solution {
    pub fn pyramid_transition(bottom: String, allowed: Vec<String>) -> bool {
        
    }
}

fn main() {
  assert_eq!(0, Solution::pyramid_transition(0));
  println!("Pass test cases!");
}
