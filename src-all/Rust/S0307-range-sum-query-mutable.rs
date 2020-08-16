/*
Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8

 
Constraints:
	The array is only modifiable by the update function.
	You may assume the number of calls to update and sumRange function is distributed evenly.
	0 <= i <= j <= nums.length - 1


*/
pub struct Solution {}
struct NumArray {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl NumArray {

    fn new(nums: Vec<i32>) -> Self {
        
    }
    
    fn update(&self, i: i32, val: i32) {
        
    }
    
    fn sum_range(&self, i: i32, j: i32) -> i32 {
        
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * let obj = NumArray::new(nums);
 * obj.update(i, val);
 * let ret_2: i32 = obj.sum_range(i, j);
 */

fn main() {
  assert_eq!(0, Solution::new(0));
  println!("Pass test cases!");
}
