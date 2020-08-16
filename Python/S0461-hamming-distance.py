"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 &le; x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       &uarr;   &uarr;

The above arrows point to positions where the corresponding bits are different.


"""
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().hammingDistance(0) == 0

