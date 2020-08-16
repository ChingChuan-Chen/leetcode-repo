"""
Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, &quot;tars&quot; and &quot;rats&quot; are similar (swapping at positions 0 and 2), and &quot;rats&quot; and &quot;arts&quot; are similar, but &quot;star&quot; is not similar to &quot;tars&quot;, &quot;rats&quot;, or &quot;arts&quot;.

Together, these form two connected groups by similarity: {&quot;tars&quot;, &quot;rats&quot;, &quot;arts&quot;} and {&quot;star&quot;}.  Notice that &quot;tars&quot; and &quot;arts&quot; are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list A of strings.  Every string in A is an anagram of every other string in A.  How many groups are there?

 
Example 1:
Input: A = ["tars","rats","arts","star"]
Output: 2

 
Constraints:
	1 <= A.length <= 2000
	1 <= A[i].length <= 1000
	A.length * A[i].length <= 20000
	All words in A consist of lowercase letters only.
	All words in A have the same length and are anagrams of each other.
	The judging time limit has been increased for this question.


"""
from typing import List
class Solution:
    def numSimilarGroups(self, A: List[str]) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().numSimilarGroups(0) == 0

