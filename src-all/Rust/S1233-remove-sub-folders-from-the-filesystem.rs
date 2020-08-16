/*
Given a list of folders, remove all sub-folders in those folders and return in any order the folders after removing.

If a folder[i] is located within another folder[j], it is called a sub-folder of it.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

 
Example 1:
Input: folder = [&quot;/a&quot;,&quot;/a/b&quot;,&quot;/c/d&quot;,&quot;/c/d/e&quot;,&quot;/c/f&quot;]
Output: [&quot;/a&quot;,&quot;/c/d&quot;,&quot;/c/f&quot;]
Explanation: Folders &quot;/a/b/&quot; is a subfolder of &quot;/a&quot; and &quot;/c/d/e&quot; is inside of folder &quot;/c/d&quot; in our filesystem.

Example 2:
Input: folder = [&quot;/a&quot;,&quot;/a/b/c&quot;,&quot;/a/b/d&quot;]
Output: [&quot;/a&quot;]
Explanation: Folders &quot;/a/b/c&quot; and &quot;/a/b/d/&quot; will be removed because they are subfolders of &quot;/a&quot;.

Example 3:
Input: folder = [&quot;/a/b/c&quot;,&quot;/a/b/ca&quot;,&quot;/a/b/d&quot;]
Output: [&quot;/a/b/c&quot;,&quot;/a/b/ca&quot;,&quot;/a/b/d&quot;]

 
Constraints:
	1 <= folder.length <= 4 * 10^4
	2 <= folder[i].length <= 100
	folder[i] contains only lowercase letters and &#39;/&#39;
	folder[i] always starts with character &#39;/&#39;
	Each folder name is unique.


*/
pub struct Solution {}
impl Solution {
    pub fn remove_subfolders(folder: Vec<String>) -> Vec<String> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::remove_subfolders(0));
  println!("Pass test cases!");
}
