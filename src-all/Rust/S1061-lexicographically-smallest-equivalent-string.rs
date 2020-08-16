/*
Given strings A and B of the same length, we say A[i] and B[i] are equivalent characters. For example, if A = &quot;abc&quot; and B = &quot;cde&quot;, then we have &#39;a&#39; == &#39;c&#39;, &#39;b&#39; == &#39;d&#39;, &#39;c&#39; == &#39;e&#39;.

Equivalent characters follow the usual rules of any equivalence relation:

	Reflexivity: &#39;a&#39; == &#39;a&#39;
	Symmetry: &#39;a&#39; == &#39;b&#39; implies &#39;b&#39; == &#39;a&#39;
	Transitivity: &#39;a&#39; == &#39;b&#39; and &#39;b&#39; == &#39;c&#39; implies &#39;a&#39; == &#39;c&#39;

For example, given the equivalency information from A and B above, S = &quot;eed&quot;, &quot;acd&quot;, and &quot;aab&quot; are equivalent strings, and &quot;aab&quot; is the lexicographically smallest equivalent string of S.

Return the lexicographically smallest equivalent string of S by using the equivalency information from A and B.

 

Example 1:
Input: A = &quot;parker&quot;, B = &quot;morris&quot;, S = &quot;parser&quot;
Output: &quot;makkek&quot;
Explanation: Based on the equivalency information in A and B, we can group their characters as [m,p], [a,o], [k,r,s], [e,i]. The characters in each group are equivalent and sorted in lexicographical order. So the answer is &quot;makkek&quot;.

Example 2:
Input: A = &quot;hello&quot;, B = &quot;world&quot;, S = &quot;hold&quot;
Output: &quot;hdld&quot;
Explanation:  Based on the equivalency information in A and B, we can group their characters as [h,w], [d,e,o], [l,r]. So only the second letter &#39;o&#39; in S is changed to &#39;d&#39;, the answer is &quot;hdld&quot;.

Example 3:
Input: A = &quot;leetcode&quot;, B = &quot;programs&quot;, S = &quot;sourcecode&quot;
Output: &quot;aauaaaaada&quot;
Explanation:  We group the equivalent characters in A and B as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in S except &#39;u&#39; and &#39;d&#39; are transformed to &#39;a&#39;, the answer is &quot;aauaaaaada&quot;.

 

Note:
	String A, B and S consist of only lowercase English letters from &#39;a&#39; - &#39;z&#39;.
	The lengths of string A, B and S are between 1 and 1000.
	String A and B are of the same length.

*/
pub struct Solution {}
impl Solution {
    pub fn smallest_equivalent_string(a: String, b: String, s: String) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::smallest_equivalent_string(0));
  println!("Pass test cases!");
}
