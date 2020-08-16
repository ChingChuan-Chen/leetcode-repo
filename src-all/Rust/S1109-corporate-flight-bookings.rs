/*
There are n flights, and they are labeled from 1 to n.

We have a list of flight bookings.  The i-th booking bookings[i] = [i, j, k] means that we booked k seats from flights labeled i to j inclusive.

Return an array answer of length n, representing the number of seats booked on each flight in order of their label.

 
Example 1:
Input: bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
Output: [10,55,45,25,25]

 
Constraints:
	1 <= bookings.length <= 20000
	1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
	1 <= bookings[i][2] <= 10000

*/
pub struct Solution {}
impl Solution {
    pub fn corp_flight_bookings(bookings: Vec<Vec<i32>>, n: i32) -> Vec<i32> {
        
    }
}

fn main() {
  assert_eq!(0, Solution::corp_flight_bookings(0));
  println!("Pass test cases!");
}
