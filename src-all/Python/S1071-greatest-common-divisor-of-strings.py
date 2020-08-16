"""
For strings S and T, we say &quot;T divides S&quot; if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

 

Example 1:
Input: str1 = &quot;ABCABC&quot;, str2 = &quot;ABC&quot;
Output: &quot;ABC&quot;

Example 2:
Input: str1 = &quot;ABABAB&quot;, str2 = &quot;ABAB&quot;
Output: &quot;AB&quot;

Example 3:
Input: str1 = &quot;LEET&quot;, str2 = &quot;CODE&quot;
Output: &quot;&quot;

 

Note:
	1 <= str1.length <= 1000
	1 <= str2.length <= 1000
	str1[i] and str2[i] are English uppercase letters.


"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().gcdOfStrings(0) == 0

