"""
Given a string s containing only digits. Return all possible valid IP addresses that can be obtained from s. You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single points and cannot have leading zeros. For example, &quot;0.1.2.201&quot; and &quot;192.168.1.1&quot; are valid IP addresses and &quot;0.011.255.245&quot;, &quot;192.168.1.312&quot; and &quot;192.168@1.1&quot; are invalid IP addresses. 

 
Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]
Example 3:
Input: s = "1111"
Output: ["1.1.1.1"]
Example 4:
Input: s = "010010"
Output: ["0.10.0.10","0.100.1.0"]
Example 5:
Input: s = "101023"
Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

 
Constraints:
	0 <= s.length <= 3000
	s consists of digits only.


"""
from typing import List
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        pass


if __name__ == '__main__':
    assert Solution().restoreIpAddresses(0) == 0

