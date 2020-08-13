// Given an input string (s) and a pattern (p), implement regular expression matching with
// support for '.' and '*'.
// '.' Matches any single character.
// '*' Matches zero or more of the preceding element.
// The matching should cover the entire input string (not partial).
//
// Note:
// s could be empty and contains only lowercase letters a-z.
// p could be empty and contains only lowercase letters a-z, and characters like . or *.
//
// Example 1:
// Input:
// s = "aa"
// p = "a"
// Output: false
// Explanation: "a" does not match the entire string "aa".
//
// Example 2:
// Input:
// s = "aa"
// p = "a*"
// Output: true
// Explanation: '*' means zero or more of the preceding element, 'a'. Therefore,
// by repeating 'a' once, it becomes "aa".
//
//
// Example 3:
// Input:
// s = "ab"
// p = ".*"
// Output: true
// Explanation: ".*" means "zero or more (*) of any character (.)".
//
//
// Example 4:
// Input:
// s = "aab"
// p = "c*a*b"
// Output: true
// Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
//
//
// Example 5:
// Input:
// s = "mississippi"
// p = "mis*is*p*."
// Output: false
pub struct Solution {}

impl Solution {
    pub fn is_match(s: String, p: String) -> bool {

    }
}

fn main() {
	assert_eq!(true, Solution::my_atoi("aa".to_string(), "a".to_string()));
    assert_eq!(true, Solution::my_atoi("aa".to_string(), "a*".to_string()));
    assert_eq!(true, Solution::my_atoi("ab".to_string(), ".*".to_string()));
    assert_eq!(true, Solution::my_atoi("az".to_string(), "a.".to_string()));
    assert_eq!(false, Solution::my_atoi("az".to_string(), "a*".to_string()));
    assert_eq!(true, Solution::my_atoi("".to_string(), "b*".to_string()));
    assert_eq!(false, Solution::my_atoi("aaa".to_string(), "".to_string()));
    assert_eq!(true, Solution::my_atoi("".to_string(), "".to_string()));
    assert_eq!(true, Solution::my_atoi("aab".to_string(), "c*a*b*".to_string()));
    assert_eq!(false, Solution::my_atoi("mississippi".to_string(), "mis*is*p*.".to_string()));
    assert_eq!(false, Solution::my_atoi("mississippi".to_string(), "mis*is*ip*.".to_string()));
	println!("Pass test cases!");
}

