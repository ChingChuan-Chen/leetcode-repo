"""
Given a url startUrl and an interface HtmlParser, implement a web crawler to crawl all links that are under the same hostname as startUrl. 

Return all urls obtained by your web crawler in any order.

Your crawler should:

	Start from the page: startUrl
	Call HtmlParser.getUrls(url) to get all urls from a webpage of given url.
	Do not crawl the same link twice.
	Explore only the links that are under the same hostname as startUrl.

As shown in the example url above, the hostname is example.org. For simplicity sake, you may assume all urls use http protocol without any port specified. For example, the urls http://leetcode.com/problems and http://leetcode.com/contest are under the same hostname, while urls http://example.org/test and http://example.com/abc are not under the same hostname.

The HtmlParser interface is defined as such: 

interface HtmlParser {
  // Return a list of all urls from a webpage of given url.
  public List<String> getUrls(String url);
}

Below are two examples explaining the functionality of the problem, for custom testing purposes you&#39;ll have three variables urls, edges and startUrl. Notice that you will only have access to startUrl in your code, while urls and edges are not directly accessible to you in code.

 
Example 1:
Input:
urls = [
  &quot;http://news.yahoo.com&quot;,
  &quot;http://news.yahoo.com/news&quot;,
  &quot;http://news.yahoo.com/news/topics/&quot;,
  &quot;http://news.google.com&quot;,
  &quot;http://news.yahoo.com/us&quot;
]
edges = [[2,0],[2,1],[3,2],[3,1],[0,4]]
startUrl = &quot;http://news.yahoo.com/news/topics/&quot;
Output: [
  &quot;http://news.yahoo.com&quot;,
  &quot;http://news.yahoo.com/news&quot;,
  &quot;http://news.yahoo.com/news/topics/&quot;,
  &quot;http://news.yahoo.com/us&quot;
]

Example 2:
Input: 
urls = [
  &quot;http://news.yahoo.com&quot;,
  &quot;http://news.yahoo.com/news&quot;,
  &quot;http://news.yahoo.com/news/topics/&quot;,
  &quot;http://news.google.com&quot;
]
edges = [[0,2],[2,1],[3,2],[3,1],[3,0]]
startUrl = &quot;http://news.google.com&quot;
Output: [&quot;http://news.google.com&quot;]
Explanation: The startUrl links to all other pages that do not share the same hostname.

 
Constraints:
	1 <= urls.length <= 1000
	1 <= urls[i].length <= 300
	startUrl is one of the urls.
	Hostname label must be from 1 to 63 characters long, including the dots, may contain only the ASCII letters from &#39;a&#39; to &#39;z&#39;, digits  from &#39;0&#39; to &#39;9&#39; and the hyphen-minus character (&#39;-&#39;).
	The hostname may not start or end with the hyphen-minus character (&#39;-&#39;). 
	See:  https://en.wikipedia.org/wiki/Hostname#Restrictions_on_valid_hostnames
	You may assume there&#39;re no duplicates in url library.


"""
from typing import List

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        
        pass


if __name__ == '__main__':
    assert Solution().crawl(0) == 0

