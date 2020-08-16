/*
Given an expression such as expression = &quot;e + 8 - a + 5&quot; and an evaluation map such as {&quot;e&quot;: 1} (given in terms of evalvars = [&quot;e&quot;] and evalints = [1]), return a list of tokens representing the simplified expression, such as [&quot;-1*a&quot;,&quot;14&quot;]

	An expression alternates chunks and symbols, with a space separating each chunk and symbol.
	A chunk is either an expression in parentheses, a variable, or a non-negative integer.
	A variable is a string of lowercase letters (not including digits.) Note that variables can be multiple letters, and note that variables never have a leading coefficient or unary operator like &quot;2x&quot; or &quot;-x&quot;.

Expressions are evaluated in the usual order: brackets first, then multiplication, then addition and subtraction. For example, expression = &quot;1 + 2 * 3&quot; has an answer of [&quot;7&quot;].

The format of the output is as follows:

	For each term of free variables with non-zero coefficient, we write the free variables within a term in sorted order lexicographically. For example, we would never write a term like &quot;b*a*c&quot;, only &quot;a*b*c&quot;.
	Terms have degree equal to the number of free variables being multiplied, counting multiplicity. (For example, &quot;a*a*b*c&quot; has degree 4.) We write the largest degree terms of our answer first, breaking ties by lexicographic order ignoring the leading coefficient of the term.
	The leading coefficient of the term is placed directly to the left with an asterisk separating it from the variables (if they exist.)  A leading coefficient of 1 is still printed.
	An example of a well formatted answer is [&quot;-2*a*a*a&quot;, &quot;3*a*a*b&quot;, &quot;3*b*b&quot;, &quot;4*a&quot;, &quot;5*c&quot;, &quot;-6&quot;] 
	Terms (including constant terms) with coefficient 0 are not included.  For example, an expression of &quot;0&quot; has an output of [].

Examples:

Input: expression = &quot;e + 8 - a + 5&quot;, evalvars = [&quot;e&quot;], evalints = [1]
Output: [&quot;-1*a&quot;,&quot;14&quot;]

Input: expression = &quot;e - 8 + temperature - pressure&quot;,
evalvars = [&quot;e&quot;, &quot;temperature&quot;], evalints = [1, 12]
Output: [&quot;-1*pressure&quot;,&quot;5&quot;]

Input: expression = &quot;(e + 8) * (e - 8)&quot;, evalvars = [], evalints = []
Output: [&quot;1*e*e&quot;,&quot;-64&quot;]

Input: expression = &quot;7 - 7&quot;, evalvars = [], evalints = []
Output: []

Input: expression = &quot;a * b * c + b * a * c * 4&quot;, evalvars = [], evalints = []
Output: [&quot;5*a*b*c&quot;]

Input: expression = &quot;((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))&quot;,
evalvars = [], evalints = []
Output: [&quot;-1*a*a*b*b&quot;,&quot;2*a*a*b*c&quot;,&quot;-1*a*a*c*c&quot;,&quot;1*a*b*b*b&quot;,&quot;-1*a*b*b*c&quot;,&quot;-1*a*b*c*c&quot;,&quot;1*a*c*c*c&quot;,&quot;-1*b*b*b*c&quot;,&quot;2*b*b*c*c&quot;,&quot;-1*b*c*c*c&quot;,&quot;2*a*a*b&quot;,&quot;-2*a*a*c&quot;,&quot;-2*a*b*b&quot;,&quot;2*a*c*c&quot;,&quot;1*b*b*b&quot;,&quot;-1*b*b*c&quot;,&quot;1*b*c*c&quot;,&quot;-1*c*c*c&quot;,&quot;-1*a*a&quot;,&quot;1*a*b&quot;,&quot;1*a*c&quot;,&quot;-1*b*c&quot;]

Note:
	expression will have length in range [1, 250].
	evalvars, evalints will have equal lengths in range [0, 100].


*/
pub struct Solution {}
impl Solution {
    pub fn basic_calculator_iv(expression: String, evalvars: Vec<String>, evalints: Vec<i32>) -> Vec<String> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::basic_calculator_iv(0));
  println!("Pass test cases!");
}
