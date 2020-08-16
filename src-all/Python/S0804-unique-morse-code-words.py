"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: &quot;a&quot; maps to &quot;.-&quot;, &quot;b&quot; maps to &quot;-...&quot;, &quot;c&quot; maps to &quot;-.-.&quot;, and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[&quot;.-&quot;,&quot;-...&quot;,&quot;-.-.&quot;,&quot;-..&quot;,&quot;.&quot;,&quot;..-.&quot;,&quot;--.&quot;,&quot;....&quot;,&quot;..&quot;,&quot;.---&quot;,&quot;-.-&quot;,&quot;.-..&quot;,&quot;--&quot;,&quot;-.&quot;,&quot;---&quot;,&quot;.--.&quot;,&quot;--.-&quot;,&quot;.-.&quot;,&quot;...&quot;,&quot;-&quot;,&quot;..-&quot;,&quot;...-&quot;,&quot;.--&quot;,&quot;-..-&quot;,&quot;-.--&quot;,&quot;--..&quot;]

Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, &quot;cab&quot; can be written as &quot;-.-..--...&quot;, (which is the concatenation &quot;-.-.&quot; + &quot;.-&quot; + &quot;-...&quot;). We&#39;ll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = [&quot;gin&quot;, &quot;zen&quot;, &quot;gig&quot;, &quot;msg&quot;]
Output: 2
Explanation: 
The transformation of each word is:
&quot;gin&quot; -> &quot;--...-.&quot;
&quot;zen&quot; -> &quot;--...-.&quot;
&quot;gig&quot; -> &quot;--...--.&quot;
&quot;msg&quot; -> &quot;--...--.&quot;

There are 2 different transformations, &quot;--...-.&quot; and &quot;--...--.&quot;.

Note:
	The length of words will be at most 100.
	Each words[i] will have length in range [1, 12].
	words[i] will only consist of lowercase letters.


"""
from typing import List
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().uniqueMorseRepresentations(0) == 0

