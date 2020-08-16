"""
(This problem is an interactive problem.)

On the sea represented by a cartesian plane, each ship is located at an integer point, and each integer point may contain at most 1 ship.

You have a function Sea.hasShips(topRight, bottomLeft) which takes two points as arguments and returns true if and only if there is at least one ship in the rectangle represented by the two points, including on the boundary.

Given two points, which are the top right and bottom left corners of a rectangle, return the number of ships present in that rectangle.  It is guaranteed that there are at most 10 ships in that rectangle.

Submissions making more than 400 calls to hasShips will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

 
Example :

Input: 
ships = [[1,1],[2,2],[3,3],[5,5]], topRight = [4,4], bottomLeft = [0,0]
Output: 3
Explanation: From [0,0] to [4,4] we can count 3 ships within the range.

 
Constraints:
	On the input ships is only given to initialize the map internally. You must solve this problem &quot;blindfolded&quot;. In other words, you must find the answer using the given hasShips API, without knowing the ships position.
	0 <= bottomLeft[0] <= topRight[0] <= 1000
	0 <= bottomLeft[1] <= topRight[1] <= 1000


"""

class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

#

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().Solution(0) == 0

