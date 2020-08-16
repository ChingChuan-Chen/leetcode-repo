/*
Implement a SnapshotArray that supports the following interface:

	SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
	void set(index, val) sets the element at the given index to be equal to val.
	int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
	int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id

 
Example 1:
Input: [&quot;SnapshotArray&quot;,&quot;set&quot;,&quot;snap&quot;,&quot;set&quot;,&quot;get&quot;]
[[3],[0,5],[],[0,6],[0,0]]
Output: [null,null,0,null,5]
Explanation: 
SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
snapshotArr.set(0,5);  // Set array[0] = 5
snapshotArr.snap();  // Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5

 
Constraints:
	1 <= length <= 50000
	At most 50000 calls will be made to set, snap, and get.
	0 <= index < length
	0 <= snap_id < (the total number of times we call snap())
	0 <= val <= 10^9


*/
pub struct Solution {}
struct SnapshotArray {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SnapshotArray {

    fn new(length: i32) -> Self {
        
    }
    
    fn set(&self, index: i32, val: i32) {
        
    }
    
    fn snap(&self) -> i32 {
        
    }
    
    fn get(&self, index: i32, snap_id: i32) -> i32 {
        
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * let obj = SnapshotArray::new(length);
 * obj.set(index, val);
 * let ret_2: i32 = obj.snap();
 * let ret_3: i32 = obj.get(index, snap_id);
 */

fn main() {
  assert_eq!(0, Solution::new(0));
  println!("Pass test cases!");
}
