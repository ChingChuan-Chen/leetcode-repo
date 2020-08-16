/*
Validate if a given string can be interpreted as a decimal number.

Some examples:
&quot;0&quot; => true
&quot; 0.1 &quot; => true
&quot;abc&quot; => false
&quot;1 a&quot; => false
&quot;2e10&quot; => true
&quot; -90e3   &quot; => true
&quot; 1e&quot; => false
&quot;e3&quot; => false
&quot; 6e-1&quot; => true
&quot; 99e2.5 &quot; => false
&quot;53.5e93&quot; => true
&quot; --6 &quot; => false
&quot;-+3&quot; => false
&quot;95a54e53&quot; => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

	Numbers 0-9
	Exponent - &quot;e&quot;
	Positive/negative sign - &quot;+&quot;/&quot;-&quot;
	Decimal point - &quot;.&quot;

Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.

*/
pub struct Solution {}
impl Solution {
    pub fn is_number(s: String) -> bool {
        
    }
}

fn main() {
  assert_eq!(0, Solution::is_number(0));
  println!("Pass test cases!");
}
