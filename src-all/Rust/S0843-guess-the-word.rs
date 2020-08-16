/*
This problem is an interactive problem new to the LeetCode platform.

We are given a word list of unique words, each word is 6 letters long, and one word in this list is chosen as secret.

You may call master.guess(word) to guess a word.  The guessed word should have type string and must be from the original list with 6 lowercase letters.

This function returns an integer type, representing the number of exact matches (value and position) of your guess to the secret word.  Also, if your guess is not in the given wordlist, it will return -1 instead.

For each test case, you have 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or less calls to master.guess and at least one of these guesses was the secret, you pass the testcase.

Besides the example test case below, there will be 5 additional test cases, each with 100 words in the word list.  The letters of each word in those testcases were chosen independently at random from &#39;a&#39; to &#39;z&#39;, such that every word in the given word lists is unique.

Example 1:
Input: secret = &quot;acckzz&quot;, wordlist = [&quot;acckzz&quot;,&quot;ccbazz&quot;,&quot;eiowzz&quot;,&quot;abcczz&quot;]

Explanation:

master.guess(&quot;aaaaaa&quot;) returns -1, because &quot;aaaaaa&quot; is not in wordlist.
master.guess(&quot;acckzz&quot;) returns 6, because &quot;acckzz&quot; is secret and has all 6 matches.
master.guess(&quot;ccbazz&quot;) returns 3, because &quot;ccbazz&quot; has 3 matches.
master.guess(&quot;eiowzz&quot;) returns 2, because &quot;eiowzz&quot; has 2 matches.
master.guess(&quot;abcczz&quot;) returns 4, because &quot;abcczz&quot; has 4 matches.

We made 5 calls to master.guess and one of them was the secret, so we pass the test case.

Note:  Any solutions that attempt to circumvent the judge will result in disqualification.

*/
