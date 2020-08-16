/*
A string such as &quot;word&quot; contains the following abbreviations:

[&quot;word&quot;, &quot;1ord&quot;, &quot;w1rd&quot;, &quot;wo1d&quot;, &quot;wor1&quot;, &quot;2rd&quot;, &quot;w2d&quot;, &quot;wo2&quot;, &quot;1o1d&quot;, &quot;1or1&quot;, &quot;w1r1&quot;, &quot;1o2&quot;, &quot;2r1&quot;, &quot;3d&quot;, &quot;w3&quot;, &quot;4&quot;]

Given a target string and a set of strings in a dictionary, find an abbreviation of this target string with the smallest possible length such that it does not conflict with abbreviations of the strings in the dictionary.

Each number or letter in the abbreviation is considered length = 1. For example, the abbreviation &quot;a32bc&quot; has length = 4.

Examples:

&quot;apple&quot;, [&quot;blade&quot;] -> &quot;a4&quot; (because &quot;5&quot; or &quot;4e&quot; conflicts with &quot;blade&quot;)

&quot;apple&quot;, [&quot;plain&quot;, &quot;amber&quot;, &quot;blade&quot;] -> &quot;1p3&quot; (other valid answers include &quot;ap3&quot;, &quot;a3e&quot;, &quot;2p2&quot;, &quot;3le&quot;, &quot;3l1&quot;).

 
Constraints:
	In the case of multiple answers as shown in the second example below, you may return any one of them.
	Assume length of target string = m, and dictionary size = n. You may assume that m &le; 21, n &le; 1000, and log2(n) + m &le; 20.


*/
pub struct Solution {}
impl Solution {
    pub fn min_abbreviation(target: String, dictionary: Vec<String>) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::min_abbreviation(0));
  println!("Pass test cases!");
}
