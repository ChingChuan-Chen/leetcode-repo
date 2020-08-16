"""
In the following, every capital letter represents some hexadecimal digit from 0 to f.

The red-green-blue color &quot;#AABBCC&quot; can be written as &quot;#ABC&quot; in shorthand.  For example, &quot;#15c&quot; is shorthand for the color &quot;#1155cc&quot;.

Now, say the similarity between two colors &quot;#ABCDEF&quot; and &quot;#UVWXYZ&quot; is -(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2.

Given the color &quot;#ABCDEF&quot;, return a 7 character color that is most similar to #ABCDEF, and has a shorthand (that is, it can be represented as some &quot;#XYZ&quot;

Example 1:
Input: color = &quot;#09f166&quot;
Output: &quot;#11ee66&quot;
Explanation:  
The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
This is the highest among any shorthand color.

Note:
	color is a string of length 7.
	color is a valid RGB color: for i > 0, color[i] is a hexadecimal digit from 0 to f
	Any answer which has the same (highest) similarity as the best answer will be accepted.
	All inputs and outputs should use lowercase letters, and the output is 7 characters.


"""
class Solution:
    def similarRGB(self, color: str) -> str:
        
        pass


if __name__ == '__main__':
    assert Solution().similarRGB(0) == 0

