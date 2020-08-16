"""
You are asked to design a file system which provides two functions:

	createPath(path, value): Creates a new path and associates a value to it if possible and returns True. Returns False if the path already exists or its parent path doesn&#39;t exist.
	get(path): Returns the value associated with a path or returns -1 if the path doesn&#39;t exist.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. For example, /leetcode and /leetcode/problems are valid paths while an empty string and / are not.

Implement the two functions.

Please refer to the examples for clarifications.

 
Example 1:
Input: 
[&quot;FileSystem&quot;,&quot;createPath&quot;,&quot;get&quot;]
[[],[&quot;/a&quot;,1],[&quot;/a&quot;]]
Output: 
[null,true,1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath(&quot;/a&quot;, 1); // return true
fileSystem.get(&quot;/a&quot;); // return 1

Example 2:
Input: 
[&quot;FileSystem&quot;,&quot;createPath&quot;,&quot;createPath&quot;,&quot;get&quot;,&quot;createPath&quot;,&quot;get&quot;]
[[],[&quot;/leet&quot;,1],[&quot;/leet/code&quot;,2],[&quot;/leet/code&quot;],[&quot;/c/d&quot;,1],[&quot;/c&quot;]]
Output: 
[null,true,true,2,false,-1]
Explanation: 
FileSystem fileSystem = new FileSystem();

fileSystem.createPath(&quot;/leet&quot;, 1); // return true
fileSystem.createPath(&quot;/leet/code&quot;, 2); // return true
fileSystem.get(&quot;/leet/code&quot;); // return 2
fileSystem.createPath(&quot;/c/d&quot;, 1); // return false because the parent path &quot;/c&quot; doesn&#39;t exist.
fileSystem.get(&quot;/c&quot;); // return -1 because this path doesn&#39;t exist.

 
Constraints:
	The number of calls to the two functions is less than or equal to 10^4 in total.
	2 <= path.length <= 100
	1 <= value <= 10^9

NOTE: create method has been changed on August 29, 2019 to createPath. Please reset to default code definition to get new method signature.

"""
class FileSystem:

    def __init__(self):
        

    def createPath(self, path: str, value: int) -> bool:
        

    def get(self, path: str) -> int:
        


# param_2 = obj.get(path)
        pass


if __name__ == '__main__':
    assert Solution().__init__(0) == 0

