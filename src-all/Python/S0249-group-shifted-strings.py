"""
Given a string, we can &quot;shift&quot; each of its letter to its successive letter, for example: &quot;abc&quot; -> &quot;bcd&quot;. We can keep &quot;shifting&quot; which forms the sequence:

&quot;abc&quot; -> &quot;bcd&quot; -> ... -> &quot;xyz&quot;

Given a list of non-empty strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

Example:

Input: [&quot;abc&quot;, &quot;bcd&quot;, &quot;acef&quot;, &quot;xyz&quot;, &quot;az&quot;, &quot;ba&quot;, &quot;a&quot;, &quot;z&quot;],
Output: 
[
  [&quot;abc&quot;,&quot;bcd&quot;,&quot;xyz&quot;],
  [&quot;az&quot;,&quot;ba&quot;],
  [&quot;acef&quot;],
  [&quot;a&quot;,&quot;z&quot;]
]


"""
from typing import List
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        pass


if __name__ == '__main__':
    assert Solution().groupStrings(0) == 0

