/*
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: &quot;a&quot; maps to &quot;.-&quot;, &quot;b&quot; maps to &quot;-...&quot;, &quot;c&quot; maps to &quot;-.-.&quot;, and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[&quot;.-&quot;,&quot;-...&quot;,&quot;-.-.&quot;,&quot;-..&quot;,&quot;.&quot;,&quot;..-.&quot;,&quot;--.&quot;,&quot;....&quot;,&quot;..&quot;,&quot;.---&quot;,&quot;-.-&quot;,&quot;.-..&quot;,&quot;--&quot;,&quot;-.&quot;,&quot;---&quot;,&quot;.--.&quot;,&quot;--.-&quot;,&quot;.-.&quot;,&quot;...&quot;,&quot;-&quot;,&quot;..-&quot;,&quot;...-&quot;,&quot;.--&quot;,&quot;-..-&quot;,&quot;-.--&quot;,&quot;--..&quot;]

Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, &quot;cab&quot; can be written as &quot;-.-..--...&quot;, (which is the concatenation &quot;-.-.&quot; + &quot;.-&quot; + &quot;-...&quot;). We&#39;ll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = [&quot;gin&quot;, &quot;zen&quot;, &quot;gig&quot;, &quot;msg&quot;]
Output: 2
Explanation: 
The transformation of each word is:
&quot;gin&quot; -> &quot;--...-.&quot;
&quot;zen&quot; -> &quot;--...-.&quot;
&quot;gig&quot; -> &quot;--...--.&quot;
&quot;msg&quot; -> &quot;--...--.&quot;

There are 2 different transformations, &quot;--...-.&quot; and &quot;--...--.&quot;.

Note:
	The length of words will be at most 100.
	Each words[i] will have length in range [1, 12].
	words[i] will only consist of lowercase letters.


*/
pub struct Solution {}
impl Solution {
    pub fn unique_morse_representations(words: Vec<String>) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::unique_morse_representations(0));
  println!("Pass test cases!");
}
