"""
You should design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

	WordDictionary() Initializes the object.
	void addWord(word) adds word to the data structure, it can be matched later.
	bool search(word) returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots &#39;.&#39; where dots can be matched with any letter.

 
Example:

Input
[&quot;WordDictionary&quot;,&quot;addWord&quot;,&quot;addWord&quot;,&quot;addWord&quot;,&quot;search&quot;,&quot;search&quot;,&quot;search&quot;,&quot;search&quot;]
[[],[&quot;bad&quot;],[&quot;dad&quot;],[&quot;mad&quot;],[&quot;pad&quot;],[&quot;bad&quot;],[&quot;.ad&quot;],[&quot;b..&quot;]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord(&quot;bad&quot;);
wordDictionary.addWord(&quot;dad&quot;);
wordDictionary.addWord(&quot;mad&quot;);
wordDictionary.search(&quot;pad&quot;); // return False
wordDictionary.search(&quot;bad&quot;); // return True
wordDictionary.search(&quot;.ad&quot;); // return True
wordDictionary.search(&quot;b..&quot;); // return True

 
Constraints:
	1 <= word.length <= 500
	word in addWord consists lower-case English letters.
	word in search consist of  &#39;.&#39; or lower-case English letters.
	At most 50000 calls will be made to addWord and search .


"""
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        


# param_2 = obj.search(word)
        pass


if __name__ == '__main__':
    assert Solution().__init__(0) == 0

