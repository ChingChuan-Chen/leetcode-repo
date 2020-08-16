/*
HTML entity parser is the parser that takes HTML code as input and replace all the entities of the special characters by the characters itself.

The special characters and their entities for HTML are:

	Quotation Mark: the entity is &amp;quot; and symbol character is ".
	Single Quote Mark: the entity is &amp;apos; and symbol character is &#39;.
	Ampersand: the entity is &amp;amp; and symbol character is &amp;.
	Greater Than Sign: the entity is &amp;gt; and symbol character is >.
	Less Than Sign: the entity is &amp;lt; and symbol character is <.
	Slash: the entity is &amp;frasl; and symbol character is /.

Given the input text string to the HTML parser, you have to implement the entity parser.

Return the text after replacing the entities by the special characters.

 
Example 1:
Input: text = "&amp;amp; is an HTML entity but &amp;ambassador; is not."
Output: "&amp; is an HTML entity but &amp;ambassador; is not."
Explanation: The parser will replace the &amp;amp; entity by &amp;

Example 2:
Input: text = "and I quote: &amp;quot;...&amp;quot;"
Output: "and I quote: \"...\""

Example 3:
Input: text = "Stay home! Practice on Leetcode :)"
Output: "Stay home! Practice on Leetcode :)"

Example 4:
Input: text = "x &amp;gt; y &amp;amp;&amp;amp; x &amp;lt; y is always false"
Output: "x > y &amp;&amp; x < y is always false"

Example 5:
Input: text = "leetcode.com&amp;frasl;problemset&amp;frasl;all"
Output: "leetcode.com/problemset/all"

 
Constraints:
	1 <= text.length <= 10^5
	The string may contain any possible characters out of all the 256 ASCII characters.


*/
pub struct Solution {}
impl Solution {
    pub fn entity_parser(text: String) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::entity_parser(0));
  println!("Pass test cases!");
}
