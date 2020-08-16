"""
Every email consists of a local name and a domain name, separated by the @ sign.

For example, in alice@leetcode.com, alice is the local name, and leetcode.com is the domain name.

Besides lowercase letters, these emails may contain &#39;.&#39;s or &#39;+&#39;s.

If you add periods (&#39;.&#39;) between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name.  For example, &quot;alice.z@leetcode.com&quot; and &quot;alicez@leetcode.com&quot; forward to the same email address.  (Note that this rule does not apply for domain names.)

If you add a plus (&#39;+&#39;) in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered, for example m.y+name@email.com will be forwarded to my@email.com.  (Again, this rule does not apply for domain names.)

It is possible to use both of these rules at the same time.

Given a list of emails, we send one email to each address in the list.  How many different addresses actually receive mails? 

 

Example 1:
Input: [&quot;test.email+alex@leetcode.com&quot;,&quot;test.e.mail+bob.cathy@leetcode.com&quot;,&quot;testemail+david@lee.tcode.com&quot;]
Output: 2
Explanation: &quot;testemail@leetcode.com&quot; and &quot;testemail@lee.tcode.com&quot; actually receive mails

 

Note:
	1 <= emails[i].length <= 100
	1 <= emails.length <= 100
	Each emails[i] contains exactly one &#39;@&#39; character.
	All local and domain names are non-empty.
	Local names do not start with a &#39;+&#39; character.


"""
from typing import List
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        pass


if __name__ == '__main__':
    assert Solution().numUniqueEmails(0) == 0

