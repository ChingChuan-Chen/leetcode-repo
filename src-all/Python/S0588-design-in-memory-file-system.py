"""
Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only contains this file&#39;s name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don&#39;t exist either, you should create them as well. This function has void return type.

addContentToFile: Given a file path and file content in string format. If the file doesn&#39;t exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.

readContentFromFile: Given a file path, return its content in string format.

 

Example:

Input: 
[&quot;FileSystem&quot;,&quot;ls&quot;,&quot;mkdir&quot;,&quot;addContentToFile&quot;,&quot;ls&quot;,&quot;readContentFromFile&quot;]
[[],[&quot;/&quot;],[&quot;/a/b/c&quot;],[&quot;/a/b/c/d&quot;,&quot;hello&quot;],[&quot;/&quot;],[&quot;/a/b/c/d&quot;]]

Output:
[null,[],null,null,[&quot;a&quot;],&quot;hello&quot;]

Explanation:

 

Note:
	You can assume all file or directory paths are absolute paths which begin with / and do not end with / except that the path is just &quot;/&quot;.
	You can assume that all operations will be passed valid parameters and users will not attempt to retrieve file content or list a directory or file that does not exist.
	You can assume that all directory names and file names only contain lower-case letters, and same names won&#39;t exist in the same directory.


"""
from typing import List
class FileSystem:

    def __init__(self):
        

    def ls(self, path: str) -> List[str]:
        

    def mkdir(self, path: str) -> None:
        

    def addContentToFile(self, filePath: str, content: str) -> None:
        

    def readContentFromFile(self, filePath: str) -> str:
        


# param_4 = obj.readContentFromFile(filePath)
        pass


if __name__ == '__main__':
    assert Solution().__init__(0) == 0

