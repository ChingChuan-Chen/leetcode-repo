/*
Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level.

Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.

 

Example 1:
Input: &quot;/home/&quot;
Output: &quot;/home&quot;
Explanation: Note that there is no trailing slash after the last directory name.

Example 2:
Input: &quot;/../&quot;
Output: &quot;/&quot;
Explanation: Going one level up from the root directory is a no-op, as the root level is the highest level you can go.

Example 3:
Input: &quot;/home//foo/&quot;
Output: &quot;/home/foo&quot;
Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

Example 4:
Input: &quot;/a/./b/../../c/&quot;
Output: &quot;/c&quot;

Example 5:
Input: &quot;/a/../../b/../c//.//&quot;
Output: &quot;/c&quot;

Example 6:
Input: &quot;/a//b////c/d//././/..&quot;
Output: &quot;/a/b/c&quot;


*/
pub struct Solution {}
impl Solution {
    pub fn simplify_path(path: String) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::simplify_path(0));
  println!("Pass test cases!");
}
