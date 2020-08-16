"""
We are given some website visits: the user with name username[i] visited the website website[i] at time timestamp[i].

A 3-sequence is a list of websites of length 3 sorted in ascending order by the time of their visits.  (The websites in a 3-sequence are not necessarily distinct.)

Find the 3-sequence visited by the largest number of users. If there is more than one solution, return the lexicographically smallest such 3-sequence.

 

Example 1:
Input: username = [&quot;joe&quot;,&quot;joe&quot;,&quot;joe&quot;,&quot;james&quot;,&quot;james&quot;,&quot;james&quot;,&quot;james&quot;,&quot;mary&quot;,&quot;mary&quot;,&quot;mary&quot;], timestamp = [1,2,3,4,5,6,7,8,9,10], website = [&quot;home&quot;,&quot;about&quot;,&quot;career&quot;,&quot;home&quot;,&quot;cart&quot;,&quot;maps&quot;,&quot;home&quot;,&quot;home&quot;,&quot;about&quot;,&quot;career&quot;]
Output: [&quot;home&quot;,&quot;about&quot;,&quot;career&quot;]
Explanation: 
The tuples in this example are:
[&quot;joe&quot;, 1, &quot;home&quot;]
[&quot;joe&quot;, 2, &quot;about&quot;]
[&quot;joe&quot;, 3, &quot;career&quot;]
[&quot;james&quot;, 4, &quot;home&quot;]
[&quot;james&quot;, 5, &quot;cart&quot;]
[&quot;james&quot;, 6, &quot;maps&quot;]
[&quot;james&quot;, 7, &quot;home&quot;]
[&quot;mary&quot;, 8, &quot;home&quot;]
[&quot;mary&quot;, 9, &quot;about&quot;]
[&quot;mary&quot;, 10, &quot;career&quot;]
The 3-sequence (&quot;home&quot;, &quot;about&quot;, &quot;career&quot;) was visited at least once by 2 users.
The 3-sequence (&quot;home&quot;, &quot;cart&quot;, &quot;maps&quot;) was visited at least once by 1 user.
The 3-sequence (&quot;home&quot;, &quot;cart&quot;, &quot;home&quot;) was visited at least once by 1 user.
The 3-sequence (&quot;home&quot;, &quot;maps&quot;, &quot;home&quot;) was visited at least once by 1 user.
The 3-sequence (&quot;cart&quot;, &quot;maps&quot;, &quot;home&quot;) was visited at least once by 1 user.

 

Note:
	3 <= N = username.length = timestamp.length = website.length <= 50
	1 <= username[i].length <= 10
	0 <= timestamp[i] <= 10^9
	1 <= website[i].length <= 10
	Both username[i] and website[i] contain only lowercase characters.
	It is guaranteed that there is at least one user who visited at least 3 websites.
	No user visits two websites at the same time.


"""
from typing import List
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        
        pass


if __name__ == '__main__':
    assert Solution().mostVisitedPattern(0) == 0

