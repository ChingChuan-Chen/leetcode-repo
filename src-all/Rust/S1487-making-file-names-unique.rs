/*
Given an array of strings names of size n. You will create n folders in your file system such that, at the ith minute, you will create a folder with the name names[i].

Since two files cannot have the same name, if you enter a folder name which is previously used, the system will have a suffix addition to its name in the form of (k), where, k is the smallest positive integer such that the obtained name remains unique.

Return an array of strings of length n where ans[i] is the actual name the system will assign to the ith folder when you create it.

 
Example 1:
Input: names = [&quot;pes&quot;,&quot;fifa&quot;,&quot;gta&quot;,&quot;pes(2019)&quot;]
Output: [&quot;pes&quot;,&quot;fifa&quot;,&quot;gta&quot;,&quot;pes(2019)&quot;]
Explanation: Let&#39;s see how the file system creates folder names:
&quot;pes&quot; --> not assigned before, remains &quot;pes&quot;
&quot;fifa&quot; --> not assigned before, remains &quot;fifa&quot;
&quot;gta&quot; --> not assigned before, remains &quot;gta&quot;
&quot;pes(2019)&quot; --> not assigned before, remains &quot;pes(2019)&quot;

Example 2:
Input: names = [&quot;gta&quot;,&quot;gta(1)&quot;,&quot;gta&quot;,&quot;avalon&quot;]
Output: [&quot;gta&quot;,&quot;gta(1)&quot;,&quot;gta(2)&quot;,&quot;avalon&quot;]
Explanation: Let&#39;s see how the file system creates folder names:
&quot;gta&quot; --> not assigned before, remains &quot;gta&quot;
&quot;gta(1)&quot; --> not assigned before, remains &quot;gta(1)&quot;
&quot;gta&quot; --> the name is reserved, system adds (k), since &quot;gta(1)&quot; is also reserved, systems put k = 2. it becomes &quot;gta(2)&quot;
&quot;avalon&quot; --> not assigned before, remains &quot;avalon&quot;

Example 3:
Input: names = [&quot;onepiece&quot;,&quot;onepiece(1)&quot;,&quot;onepiece(2)&quot;,&quot;onepiece(3)&quot;,&quot;onepiece&quot;]
Output: [&quot;onepiece&quot;,&quot;onepiece(1)&quot;,&quot;onepiece(2)&quot;,&quot;onepiece(3)&quot;,&quot;onepiece(4)&quot;]
Explanation: When the last folder is created, the smallest positive valid k is 4, and it becomes &quot;onepiece(4)&quot;.

Example 4:
Input: names = [&quot;wano&quot;,&quot;wano&quot;,&quot;wano&quot;,&quot;wano&quot;]
Output: [&quot;wano&quot;,&quot;wano(1)&quot;,&quot;wano(2)&quot;,&quot;wano(3)&quot;]
Explanation: Just increase the value of k each time you create folder &quot;wano&quot;.

Example 5:
Input: names = [&quot;kaido&quot;,&quot;kaido(1)&quot;,&quot;kaido&quot;,&quot;kaido(1)&quot;]
Output: [&quot;kaido&quot;,&quot;kaido(1)&quot;,&quot;kaido(2)&quot;,&quot;kaido(1)(1)&quot;]
Explanation: Please note that system adds the suffix (k) to current name even it contained the same suffix before.

 
Constraints:
	1 <= names.length <= 5 * 10^4
	1 <= names[i].length <= 20
	names[i] consists of lower case English letters, digits and/or round brackets.

*/
pub struct Solution {}
impl Solution {
    pub fn get_folder_names(names: Vec<String>) -> Vec<String> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::get_folder_names(0));
  println!("Pass test cases!");
}
