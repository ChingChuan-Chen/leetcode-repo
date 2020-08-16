/*
A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to &quot;Goat Latin&quot; (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

	If a word begins with a vowel (a, e, i, o, or u), append &quot;ma&quot; to the end of the word.
	For example, the word &#39;apple&#39; becomes &#39;applema&#39;.
	 
	If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add &quot;ma&quot;.
	For example, the word &quot;goat&quot; becomes &quot;oatgma&quot;.
	 
	Add one letter &#39;a&#39; to the end of each word per its word index in the sentence, starting with 1.
	For example, the first word gets &quot;a&quot; added to the end, the second word gets &quot;aa&quot; added to the end and so on.

Return the final sentence representing the conversion from S to Goat Latin. 

 

Example 1:
Input: &quot;I speak Goat Latin&quot;
Output: &quot;Imaa peaksmaaa oatGmaaaa atinLmaaaaa&quot;

Example 2:
Input: &quot;The quick brown fox jumped over the lazy dog&quot;
Output: &quot;heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa&quot;

 

Notes:

	S contains only uppercase, lowercase and spaces. Exactly one space between each word.
	1 <= S.length <= 150.


*/
pub struct Solution {}
impl Solution {
    pub fn to_goat_latin(s: String) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::to_goat_latin(0));
  println!("Pass test cases!");
}
