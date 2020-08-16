"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false

 
Constraints:
	s consists only of printable ASCII characters.


"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        low = 0
        high = len(s)-1
        while low < high:
            while low < len(s) and not s[low].isalnum():
                low += 1
                if low == len(s):
                    return True
            while high > 0 and not s[high].isalnum():
                high -= 1
            if s[low].lower() != s[high].lower():
                return False
            else:
                low += 1
                high -= 1
        return True

if __name__ == '__main__':
    assert Solution().isPalindrome("A man, a plan, a canal: Panama") == True
    assert Solution().isPalindrome("race a car") == False
    assert Solution().isPalindrome("") == True
    assert Solution().isPalindrome("a") == True
    assert Solution().isPalindrome("aa") == True
    assert Solution().isPalindrome("aba") == True
    assert Solution().isPalindrome(".,") == True
    assert Solution().isPalindrome("0P") == False
    assert Solution().isPalindrome("0P0") == True
