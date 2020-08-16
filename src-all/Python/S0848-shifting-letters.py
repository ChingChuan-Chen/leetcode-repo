"""
We have a string S of lowercase letters, and an integer array shifts.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so that &#39;z&#39; becomes &#39;a&#39;). 

For example, shift(&#39;a&#39;) = &#39;b&#39;, shift(&#39;t&#39;) = &#39;u&#39;, and shift(&#39;z&#39;) = &#39;a&#39;.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to S are applied.

Example 1:
Input: S = &quot;abc&quot;, shifts = [3,5,9]
Output: &quot;rpl&quot;
Explanation: 
We start with &quot;abc&quot;.
After shifting the first 1 letters of S by 3, we have &quot;dbc&quot;.
After shifting the first 2 letters of S by 5, we have &quot;igc&quot;.
After shifting the first 3 letters of S by 9, we have &quot;rpl&quot;, the answer.

Note:
	1 <= S.length = shifts.length <= 20000
	0 <= shifts[i] <= 10 ^ 9


"""
from typing import List
class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().shiftingLetters(0) == 0

