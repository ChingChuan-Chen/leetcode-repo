/*
In English, we have a concept called root, which can be followed by some other words to form another longer word - let&#39;s call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

 
Example 1:
Input: dict = [&quot;cat&quot;,&quot;bat&quot;,&quot;rat&quot;], sentence = &quot;the cattle was rattled by the battery&quot;
Output: &quot;the cat was rat by the bat&quot;

 
Constraints:
	The input will only have lower-case letters.
	1 <= dict.length <= 1000
	1 <= dict[i].length <= 100
	1 <= sentence words number <= 1000
	1 <= sentence words length <= 1000


*/
pub struct Solution {}
impl Solution {
    pub fn replace_words(dict: Vec<String>, sentence: String) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::replace_words(0));
  println!("Pass test cases!");
}
