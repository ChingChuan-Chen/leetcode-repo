/*
Given a string IP. We need to check If IP is a valid IPv4 address, valid IPv6 address or not a valid IP address.

Return &quot;IPv4&quot; if IP is a valid IPv4 address, &quot;IPv6&quot; if IP is a valid IPv6 address or &quot;Neither&quot; if IP is not a valid IP of any type.

A valid IPv4 address is an IP in the form &quot;x1.x2.x3.x4&quot; where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, &quot;192.168.1.1&quot; and &quot;192.168.1.0&quot; are valid IPv4 addresses but &quot;192.168.01.1&quot;, &quot;192.168.1.00&quot; and &quot;192.168@1.1&quot; are invalid IPv4 adresses.

A valid IPv6 address is an IP in the form &quot;x1:x2:x3:x4:x5:x6:x7:x8&quot; where:

	1 <= xi.length <= 4
	xi is hexadecimal string whcih may contain digits, lower-case English letter (&#39;a&#39; to &#39;f&#39;) and/or upper-case English letters (&#39;A&#39; to &#39;F&#39;).
	Leading zeros are allowed in xi.

For example, &quot;2001:0db8:85a3:0000:0000:8a2e:0370:7334&quot; and &quot;2001:db8:85a3:0:0:8A2E:0370:7334&quot; are valid IPv6 addresses but &quot;2001:0db8:85a3::8A2E:037j:7334&quot; and &quot;02001:0db8:85a3:0000:0000:8a2e:0370:7334&quot; are invalid IPv6 addresses.

 
Example 1:
Input: IP = &quot;172.16.254.1&quot;
Output: &quot;IPv4&quot;
Explanation: This is a valid IPv4 address, return &quot;IPv4&quot;.

Example 2:
Input: IP = &quot;2001:0db8:85a3:0:0:8A2E:0370:7334&quot;
Output: &quot;IPv6&quot;
Explanation: This is a valid IPv6 address, return &quot;IPv6&quot;.

Example 3:
Input: IP = &quot;256.256.256.256&quot;
Output: &quot;Neither&quot;
Explanation: This is neither a IPv4 address nor a IPv6 address.

Example 4:
Input: IP = &quot;2001:0db8:85a3:0:0:8A2E:0370:7334:&quot;
Output: &quot;Neither&quot;

Example 5:
Input: IP = &quot;1e1.4.5.6&quot;
Output: &quot;Neither&quot;

 
Constraints:
	IP consists only of English letters, digits and the characters &#39;.&#39; and &#39;:&#39;.


*/
pub struct Solution {}
impl Solution {
    pub fn valid_ip_address(ip: String) -> String {
        
    }
}

fn main() {
  assert_eq!(0, Solution::valid_ip_address(0));
  println!("Pass test cases!");
}
