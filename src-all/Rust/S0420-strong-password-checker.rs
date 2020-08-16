/*
A password is considered strong if below conditions are all met:

 It has at least 6 characters and at most 20 characters. 
 It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit. 
 It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met). 

Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.

Insertion, deletion or replace of any one character are all considered as one change.
*/
pub struct Solution {}
impl Solution {
    pub fn strong_password_checker(s: String) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::strong_password_checker(0));
  println!("Pass test cases!");
}
