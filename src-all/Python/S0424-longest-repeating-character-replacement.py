"""
Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

Note:
Both the string&#39;s length and k will not exceed 104.

Example 1:
Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two &#39;A&#39;s with two &#39;B&#39;s or vice versa.

 

Example 2:
Input:
s = "AABABBA", k = 1

Output:
4

Explanation:
Replace the one &#39;A&#39; in the middle with &#39;B&#39; and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

 

"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().characterReplacement(0) == 0

