// Implement atoi which converts a string to an integer.
//
// The function first discards as many whitespace characters as necessary until the first
// non-whitespace character is found. Then, starting from this character,
// takes an optional initial plus or minus sign followed by as many numerical digits as possible,
// and interprets them as a numerical value.
//
// The string can contain additional characters after those that form the integral number,
// which are ignored and have no effect on the behavior of this function.
//
// If the first sequence of non-whitespace characters in str is not a valid integral number,
// or if no such sequence exists because either str is empty or it contains only whitespace
// characters, no conversion is performed.
//
// If no valid conversion could be performed, a zero value is returned.
//
// Note:
// Only the space character ' ' is considered as whitespace character.
// Assume we are dealing with an environment which could only store integers within the 32-bit
// signed integer range: [−2^31, 2^31 − 1]. If the numerical value is out of the range of
// representable values, INT_MAX (2^31 − 1) or INT_MIN (−2^31) is returned.
//
//
// Example 1:
// Input: "42"
// Output: 42
//
// Example 2:
// Input: "   -42"
// Output: -42
// Explanation: The first non-whitespace character is '-', which is the minus sign.
//              Then take as many numerical digits as possible, which gets 42.
//
// Example 3:
// Input: "4193 with words"
// Output: 4193
// Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
//
//
// Example 4:
// Input: "words and 987"
// Output: 0
// Explanation: The first non-whitespace character is 'w', which is not a numerical digit or
//              a +/- sign. Therefore no valid conversion could be performed.
//
// Example 5:
// Input: "-91283472332"
// Output: -2147483648
// Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
//              Therefore INT_MIN (−231) is returned.

pub struct Solution {}

impl Solution {
    pub fn my_atoi(str: String) -> i32 {
	    let n = str.len();
	    let chars: Vec<char> = str.chars().collect();
	    if n == 0 {
		    return 0;
	    }
	    let mut start_idx = -1;
        let mut sign = 1;
		for (idx, ch) in chars.iter().enumerate() {
			match ch {
				' ' => {},
				'0'..='9' => {
					start_idx = idx as i32;
					break;
				},
				'+' => {
					start_idx = idx as i32;
					break;
				},
				'-' => {
                    sign = -1;
					start_idx = idx as i32;
					break;
				},
				_ => return 0
			}
	    }
	    if start_idx == -1 {
		    return 0;
	    }
        let mut res = 0i64;
        match chars[start_idx as usize] {
            '0'..='9' => {
                res = chars[start_idx as usize].to_digit(10).unwrap() as i64;
            },
            _ => {}
        }

	    let mut end_idx = (start_idx as usize) + 1;
	    while end_idx < n {
			match chars[end_idx] {
				'0'..='9' => {
					res *= 10;
					res += chars[end_idx].to_digit(10).unwrap() as i64;
                    if res > std::i32::MAX as i64 {
                        break;
                    }
				},
				_ => {
					break;
				}
			}
            end_idx += 1;
	    }
        res *= sign;
		if res > std::i32::MAX as i64 {
            return std::i32::MAX;
        }
        if res < std::i32::MIN as i64 {
            return std::i32::MIN;
        }
	    return res as i32;
    }
}

fn main() {
	assert_eq!(4, Solution::my_atoi("4".to_string()));
	assert_eq!(42, Solution::my_atoi("42".to_string()));
	assert_eq!(-42, Solution::my_atoi("   -42".to_string()));
	assert_eq!(0, Solution::my_atoi("   --42".to_string()));
	assert_eq!(0, Solution::my_atoi("   ++42".to_string()));
	assert_eq!(0, Solution::my_atoi("   +-42".to_string()));
	assert_eq!(0, Solution::my_atoi("+".to_string()));
	assert_eq!(0, Solution::my_atoi("    +".to_string()));
	assert_eq!(0, Solution::my_atoi("".to_string()));
	assert_eq!(4193, Solution::my_atoi("4193 with words".to_string()));
	assert_eq!(0, Solution::my_atoi("words and 987".to_string()));
	assert_eq!(-2147483648, Solution::my_atoi("-91283472332".to_string()));
	println!("Pass test cases!");
}

