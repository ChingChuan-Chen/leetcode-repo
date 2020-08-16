"""
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

Example:

Input: s = "++++"
Output: true 
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Follow up:
Derive your algorithm&#39;s runtime complexity.
"""
class Solution:
    def canWin(self, s: str) -> bool:
        
        pass


if __name__ == '__main__':
    assert Solution().canWin(0) == 0

