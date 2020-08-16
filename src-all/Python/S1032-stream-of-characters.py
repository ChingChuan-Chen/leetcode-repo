"""
Implement the StreamChecker class as follows:

	StreamChecker(words): Constructor, init the data structure with the given words.
	query(letter): returns true if and only if for some k >= 1, the last k characters queried (in order from oldest to newest, including this letter just queried) spell one of the words in the given list.

 

Example:

StreamChecker streamChecker = new StreamChecker([&quot;cd&quot;,&quot;f&quot;,&quot;kl&quot;]); // init the dictionary.
streamChecker.query(&#39;a&#39;);          // return false
streamChecker.query(&#39;b&#39;);          // return false
streamChecker.query(&#39;c&#39;);          // return false
streamChecker.query(&#39;d&#39;);          // return true, because &#39;cd&#39; is in the wordlist
streamChecker.query(&#39;e&#39;);          // return false
streamChecker.query(&#39;f&#39;);          // return true, because &#39;f&#39; is in the wordlist
streamChecker.query(&#39;g&#39;);          // return false
streamChecker.query(&#39;h&#39;);          // return false
streamChecker.query(&#39;i&#39;);          // return false
streamChecker.query(&#39;j&#39;);          // return false
streamChecker.query(&#39;k&#39;);          // return false
streamChecker.query(&#39;l&#39;);          // return true, because &#39;kl&#39; is in the wordlist

 

Note:
	1 <= words.length <= 2000
	1 <= words[i].length <= 2000
	Words will only consist of lowercase English letters.
	Queries will only consist of lowercase English letters.
	The number of queries is at most 40000.


"""
from typing import List
class StreamChecker:

    def __init__(self, words: List[str]):
        

    def query(self, letter: str) -> bool:
        


# param_1 = obj.query(letter)
        pass


if __name__ == '__main__':
    assert Solution().__init__(0) == 0

