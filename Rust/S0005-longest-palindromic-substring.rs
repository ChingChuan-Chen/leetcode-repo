// Given a string s, find the longest palindromic substring in s.
// You may assume that the maximum length of s is 1000.
//
// Example 1:
// Input: "babad"
// Output: "bab"
// Note: "aba" is also a valid answer.
//
// Example 2:
// Input: "cbbd"
// Output: "bb"
pub struct Solution {}

impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        let n = s.len();
        if n <= 1 {
            return s
        }
        let chars: Vec<char> = s.chars().collect();
        let (mut start, mut max_len) = (0, 1);
        let mut is_palindromic = vec![vec![false; n]; n];
        let mut j: usize = 0;
        for i in 0..n {
            j = i;
            loop {
                if chars[i] == chars[j] && (i-j<2 || is_palindromic[j+1][i-1]){
                    is_palindromic[j][i] = true;
                    if max_len < i-j+1 {
                        start = j;
                        max_len = i-j+1;
                    }
                }
                if j == 0 {
                    break;
                }
                j -= 1;
            }
        }
        return s[start..(start+max_len)].to_owned()
    }
}

fn main() {
    assert_eq!("bab".to_string(), Solution::longestPalindrome("babad".to_string()));
    assert_eq!("abccba".to_string(), Solution::longestPalindrome("cbbd".to_string()));
    assert_eq!("abccba".to_string(), Solution::longestPalindrome("abccba".to_string()));
    assert_eq!("abcAcba".to_string(), Solution::longestPalindrome("abcAcba".to_string()));
    assert_eq!("".to_string(), Solution::longestPalindrome("".to_string()));
    assert_eq!("a".to_string(), Solution::longestPalindrome("a".to_string()));
    println!("Pass test cases!");
}

