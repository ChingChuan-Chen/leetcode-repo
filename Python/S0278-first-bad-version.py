"""
You are a product manager and currently leading a team to develop a new product.
Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous version,
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad.
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:
Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
"""

def isBadVersion(version):
    if version >= 12:
        raise Exception("Must be less than 6")
    if version >= 4:
        return True
    else:
        return False


class Solution:
    def firstBadVersion(self, n) -> bool:
        low, high = 1, n
        while low < high:
            i = (low + high) // 2
            if isBadVersion(i):
                high = i
            else:
                low = i + 1
        return low


if __name__ == '__main__':
    assert Solution().firstBadVersion(4) == 4
    assert Solution().firstBadVersion(5) == 4
    assert Solution().firstBadVersion(6) == 4
    assert Solution().firstBadVersion(7) == 4
    assert Solution().firstBadVersion(8) == 4
    assert Solution().firstBadVersion(9) == 4
    assert Solution().firstBadVersion(10) == 4
    assert Solution().firstBadVersion(11) == 4