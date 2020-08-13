// Given a string, find the length of the longest substring without repeating characters.
//
//
// Example 1:
// Input: "abcabcbb"
// Output: 3
// Explanation: The answer is "abc", with the length of 3.
//
// Example 2:
// Input: "bbbbb"
// Output: 1
// Explanation: The answer is "b", with the length of 1.
//
// Example 3:
// Input: "pwwkew"
// Output: 3
// Explanation: The answer is "wke", with the length of 3.
// Note that the answer must be a substring, "pwke" is a subsequence
// and not a substring.
pub struct Solution {}

use std::collections::HashMap;
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut used_chars: HashMap<char, usize> = HashMap::new();
        let mut start: usize = 0;
        let mut max_len: usize = 0;
        let characters: Vec<char> = s.chars().collect();
        for (index, character) in characters.iter().enumerate() {
            if used_chars.contains_key(character) && start <= *used_chars.get(character).unwrap() {
                start = *used_chars.get(character).unwrap() + 1;
            } else {
                max_len = max_len.max(index - start + 1);
            }
            used_chars.insert(*character, index);
        }
        return max_len as i32;
    }
}

fn main() {
    assert_eq!(3, Solution::length_of_longest_substring("abcabcbb".to_string()));
    assert_eq!(1, Solution::length_of_longest_substring("bbbbb".to_string()));
    assert_eq!(3, Solution::length_of_longest_substring("pwwkew".to_string()));
    assert_eq!(0, Solution::length_of_longest_substring("".to_string()));
    println!("Pass test cases!");
}

