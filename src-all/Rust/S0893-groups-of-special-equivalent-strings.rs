/*
You are given an array A of strings.

A move onto S consists of swapping any two even indexed characters of S, or any two odd indexed characters of S.

Two strings S and T are special-equivalent if after any number of moves onto S, S == T.

For example, S = &quot;zzxy&quot; and T = &quot;xyzz&quot; are special-equivalent because we may make the moves &quot;zzxy&quot; -> &quot;xzzy&quot; -> &quot;xyzz&quot; that swap S[0] and S[2], then S[1] and S[3].

Now, a group of special-equivalent strings from A is a non-empty subset of A such that:

	Every pair of strings in the group are special equivalent, and;
	The group is the largest size possible (ie., there isn&#39;t a string S not in the group such that S is special equivalent to every string in the group)

Return the number of groups of special-equivalent strings from A.

 

Example 1:
Input: [&quot;abcd&quot;,&quot;cdab&quot;,&quot;cbad&quot;,&quot;xyzz&quot;,&quot;zzxy&quot;,&quot;zzyx&quot;]
Output: 3
Explanation: 
One group is [&quot;abcd&quot;, &quot;cdab&quot;, &quot;cbad&quot;], since they are all pairwise special equivalent, and none of the other strings are all pairwise special equivalent to these.

The other two groups are [&quot;xyzz&quot;, &quot;zzxy&quot;] and [&quot;zzyx&quot;].  Note that in particular, &quot;zzxy&quot; is not special equivalent to &quot;zzyx&quot;.

Example 2:
Input: [&quot;abc&quot;,&quot;acb&quot;,&quot;bac&quot;,&quot;bca&quot;,&quot;cab&quot;,&quot;cba&quot;]
Output: 3

 

Note:
	1 <= A.length <= 1000
	1 <= A[i].length <= 20
	All A[i] have the same length.
	All A[i] consist of only lowercase letters.


*/
pub struct Solution {}
impl Solution {
    pub fn num_special_equiv_groups(a: Vec<String>) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::num_special_equiv_groups(0));
  println!("Pass test cases!");
}
