"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces &#39; &#39; when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:
	A word is defined as a character sequence consisting of non-space characters only.
	Each word&#39;s length is guaranteed to be greater than 0 and not exceed maxWidth.
	The input array words contains at least one word.

Example 1:
Input:
words = [&quot;This&quot;, &quot;is&quot;, &quot;an&quot;, &quot;example&quot;, &quot;of&quot;, &quot;text&quot;, &quot;justification.&quot;]
maxWidth = 16
Output:
[
   &quot;This    is    an&quot;,
   &quot;example  of text&quot;,
   &quot;justification.  &quot;
]

Example 2:
Input:
words = [&quot;What&quot;,&quot;must&quot;,&quot;be&quot;,&quot;acknowledgment&quot;,&quot;shall&quot;,&quot;be&quot;]
maxWidth = 16
Output:
[
  &quot;What   must   be&quot;,
  &quot;acknowledgment  &quot;,
  &quot;shall be        &quot;
]
Explanation: Note that the last line is &quot;shall be    &quot; instead of &quot;shall     be&quot;,
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.

Example 3:
Input:
words = [&quot;Science&quot;,&quot;is&quot;,&quot;what&quot;,&quot;we&quot;,&quot;understand&quot;,&quot;well&quot;,&quot;enough&quot;,&quot;to&quot;,&quot;explain&quot;,
         &quot;to&quot;,&quot;a&quot;,&quot;computer.&quot;,&quot;Art&quot;,&quot;is&quot;,&quot;everything&quot;,&quot;else&quot;,&quot;we&quot;,&quot;do&quot;]
maxWidth = 20
Output:
[
  &quot;Science  is  what we&quot;,
  &quot;understand      well&quot;,
  &quot;enough to explain to&quot;,
  &quot;a  computer.  Art is&quot;,
  &quot;everything  else  we&quot;,
  &quot;do                  &quot;
]


"""
from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        
        pass


if __name__ == '__main__':
    assert Solution().fullJustify(0) == 0

