/*
Suppose you are given the following code:

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print(&quot;foo&quot;);
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print(&quot;bar&quot;);
    }
  }
}

The same instance of FooBar will be passed to two different threads. Thread A will call foo() while thread B will call bar(). Modify the given program to output &quot;foobar&quot; n times.

 

Example 1:
Input: n = 1
Output: &quot;foobar&quot;
Explanation: There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar(). &quot;foobar&quot; is being output 1 time.

Example 2:
Input: n = 2
Output: &quot;foobarfoobar&quot;
Explanation: &quot;foobar&quot; is being output 2 times.


*/
