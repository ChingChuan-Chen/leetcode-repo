"""


You have a keyboard layout as shown above in the XY plane, where each English uppercase letter is located at some coordinate, for example, the letter A is located at coordinate (0,0), the letter B is located at coordinate (0,1), the letter P is located at coordinate (2,3) and the letter Z is located at coordinate (4,1).

Given the string word, return the minimum total distance to type such string using only two fingers. The distance between coordinates (x1,y1) and (x2,y2) is |x1 - x2| + |y1 - y2|. 

Note that the initial positions of your two fingers are considered free so don&#39;t count towards your total distance, also your two fingers do not have to start at the first letter or the first two letters.

 
Example 1:
Input: word = &quot;CAKE&quot;
Output: 3
Explanation: 
Using two fingers, one optimal way to type &quot;CAKE&quot; is: 
Finger 1 on letter &#39;C&#39; -> cost = 0 
Finger 1 on letter &#39;A&#39; -> cost = Distance from letter &#39;C&#39; to letter &#39;A&#39; = 2 
Finger 2 on letter &#39;K&#39; -> cost = 0 
Finger 2 on letter &#39;E&#39; -> cost = Distance from letter &#39;K&#39; to letter &#39;E&#39; = 1 
Total distance = 3

Example 2:
Input: word = &quot;HAPPY&quot;
Output: 6
Explanation: 
Using two fingers, one optimal way to type &quot;HAPPY&quot; is:
Finger 1 on letter &#39;H&#39; -> cost = 0
Finger 1 on letter &#39;A&#39; -> cost = Distance from letter &#39;H&#39; to letter &#39;A&#39; = 2
Finger 2 on letter &#39;P&#39; -> cost = 0
Finger 2 on letter &#39;P&#39; -> cost = Distance from letter &#39;P&#39; to letter &#39;P&#39; = 0
Finger 1 on letter &#39;Y&#39; -> cost = Distance from letter &#39;A&#39; to letter &#39;Y&#39; = 4
Total distance = 6

Example 3:
Input: word = &quot;NEW&quot;
Output: 3

Example 4:
Input: word = &quot;YEAR&quot;
Output: 7

 
Constraints:
	2 <= word.length <= 300
	Each word[i] is an English uppercase letter.

"""
class Solution:
    def minimumDistance(self, word: str) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().minimumDistance(0) == 0

