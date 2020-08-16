/*
An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
     &darr;
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
     &darr;   &darr;    &darr;    &darr;  &darr;    
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
     &darr;   &darr;    &darr;
d) l|ocalizatio|n          --> l10n

Additionally for any string s of size less than or equal to 2 their abbreviation is the same string s.

Find whether its abbreviation is unique in the dictionary. A word&#39;s abbreviation is called unique if any of the following conditions is met:

	There is no word in dictionary such that their abbreviation is equal to the abbreviation of word.
	Else, for all words in dictionary such that their abbreviation is equal to the abbreviation of word those words are equal to word.

 
Example 1:
Input
[&quot;ValidWordAbbr&quot;,&quot;isUnique&quot;,&quot;isUnique&quot;,&quot;isUnique&quot;,&quot;isUnique&quot;]
[[[&quot;deer&quot;,&quot;door&quot;,&quot;cake&quot;,&quot;card&quot;]],[&quot;dear&quot;],[&quot;cart&quot;],[&quot;cane&quot;],[&quot;make&quot;]]
Output
[null,false,true,false,true]

Explanation
ValidWordAbbr validWordAbbr = new ValidWordAbbr([&quot;deer&quot;, &quot;door&quot;, &quot;cake&quot;, &quot;card&quot;]);
validWordAbbr.isUnique(&quot;dear&quot;); // return False
validWordAbbr.isUnique(&quot;cart&quot;); // return True
validWordAbbr.isUnique(&quot;cane&quot;); // return False
validWordAbbr.isUnique(&quot;make&quot;); // return True

 
Constraints:
	Each word will only consist of lowercase English characters.


*/
pub struct Solution {}
struct ValidWordAbbr {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ValidWordAbbr {

    fn new(dictionary: Vec<String>) -> Self {
        
    }
    
    fn is_unique(&self, word: String) -> bool {
        
    }
}

/**
 * Your ValidWordAbbr object will be instantiated and called as such:
 * let obj = ValidWordAbbr::new(dictionary);
 * let ret_1: bool = obj.is_unique(word);
 */

fn main() {
  assert_eq!(0, Solution::new(0));
  println!("Pass test cases!");
}
