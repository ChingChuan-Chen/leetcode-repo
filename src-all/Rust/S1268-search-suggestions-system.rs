/*
Given an array of strings products and a string searchWord. We want to design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with the searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed. 

 
Example 1:
Input: products = [&quot;mobile&quot;,&quot;mouse&quot;,&quot;moneypot&quot;,&quot;monitor&quot;,&quot;mousepad&quot;], searchWord = &quot;mouse&quot;
Output: [
[&quot;mobile&quot;,&quot;moneypot&quot;,&quot;monitor&quot;],
[&quot;mobile&quot;,&quot;moneypot&quot;,&quot;monitor&quot;],
[&quot;mouse&quot;,&quot;mousepad&quot;],
[&quot;mouse&quot;,&quot;mousepad&quot;],
[&quot;mouse&quot;,&quot;mousepad&quot;]
]
Explanation: products sorted lexicographically = [&quot;mobile&quot;,&quot;moneypot&quot;,&quot;monitor&quot;,&quot;mouse&quot;,&quot;mousepad&quot;]
After typing m and mo all products match and we show user [&quot;mobile&quot;,&quot;moneypot&quot;,&quot;monitor&quot;]
After typing mou, mous and mouse the system suggests [&quot;mouse&quot;,&quot;mousepad&quot;]

Example 2:
Input: products = [&quot;havana&quot;], searchWord = &quot;havana&quot;
Output: [[&quot;havana&quot;],[&quot;havana&quot;],[&quot;havana&quot;],[&quot;havana&quot;],[&quot;havana&quot;],[&quot;havana&quot;]]

Example 3:
Input: products = [&quot;bags&quot;,&quot;baggage&quot;,&quot;banner&quot;,&quot;box&quot;,&quot;cloths&quot;], searchWord = &quot;bags&quot;
Output: [[&quot;baggage&quot;,&quot;bags&quot;,&quot;banner&quot;],[&quot;baggage&quot;,&quot;bags&quot;,&quot;banner&quot;],[&quot;baggage&quot;,&quot;bags&quot;],[&quot;bags&quot;]]

Example 4:
Input: products = [&quot;havana&quot;], searchWord = &quot;tatiana&quot;
Output: [[],[],[],[],[],[],[]]

 
Constraints:
	1 <= products.length <= 1000
	There are no repeated elements in products.
	1 <= &Sigma; products[i].length <= 2 * 10^4
	All characters of products[i] are lower-case English letters.
	1 <= searchWord.length <= 1000
	All characters of searchWord are lower-case English letters.


*/
pub struct Solution {}
impl Solution {
    pub fn suggested_products(products: Vec<String>, search_word: String) -> Vec<Vec<String>> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::suggested_products(0));
  println!("Pass test cases!");
}
