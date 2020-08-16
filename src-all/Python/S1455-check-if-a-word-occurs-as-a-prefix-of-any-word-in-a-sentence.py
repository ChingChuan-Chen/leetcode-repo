"""
Given a sentence that consists of some words separated by a single space, and a searchWord.

You have to check if searchWord is a prefix of any word in sentence.

Return the index of the word in sentence where searchWord is a prefix of this word (1-indexed).

If searchWord is a prefix of more than one word, return the index of the first word (minimum index). If there is no such word return -1.

A prefix of a string S is any leading contiguous substring of S.

 
Example 1:
Input: sentence = &quot;i love eating burger&quot;, searchWord = &quot;burg&quot;
Output: 4
Explanation: &quot;burg&quot; is prefix of &quot;burger&quot; which is the 4th word in the sentence.

Example 2:
Input: sentence = &quot;this problem is an easy problem&quot;, searchWord = &quot;pro&quot;
Output: 2
Explanation: &quot;pro&quot; is prefix of &quot;problem&quot; which is the 2nd and the 6th word in the sentence, but we return 2 as it&#39;s the minimal index.

Example 3:
Input: sentence = &quot;i am tired&quot;, searchWord = &quot;you&quot;
Output: -1
Explanation: &quot;you&quot; is not a prefix of any word in the sentence.

Example 4:
Input: sentence = &quot;i use triple pillow&quot;, searchWord = &quot;pill&quot;
Output: 4

Example 5:
Input: sentence = &quot;hello from the other side&quot;, searchWord = &quot;they&quot;
Output: -1

 
Constraints:
	1 <= sentence.length <= 100
	1 <= searchWord.length <= 10
	sentence consists of lowercase English letters and spaces.
	searchWord consists of lowercase English letters.


"""
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().isPrefixOfWord(0) == 0

