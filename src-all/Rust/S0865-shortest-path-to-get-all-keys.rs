/*
We are given a 2-dimensional grid. &quot;.&quot; is an empty cell, &quot;#&quot; is a wall, &quot;@&quot; is the starting point, (&quot;a&quot;, &quot;b&quot;, ...) are keys, and (&quot;A&quot;, &quot;B&quot;, ...) are locks.

We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.  We cannot walk outside the grid, or walk into a wall.  If we walk over a key, we pick it up.  We can&#39;t walk over a lock unless we have the corresponding key.

For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the first K letters of the English alphabet in the grid.  This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys.  If it&#39;s impossible, return -1.

 

Example 1:
Input: [&quot;@.a.#&quot;,&quot;###.#&quot;,&quot;b.A.B&quot;]
Output: 8

Example 2:
Input: [&quot;@..aA&quot;,&quot;..B#.&quot;,&quot;....b&quot;]
Output: 6

 

Note:
	1 <= grid.length <= 30
	1 <= grid[0].length <= 30
	grid[i][j] contains only &#39;.&#39;, &#39;#&#39;, &#39;@&#39;, &#39;a&#39;-&#39;f&#39; and &#39;A&#39;-&#39;F&#39;
	The number of keys is in [1, 6].  Each key has a different letter and opens exactly one lock.


*/
pub struct Solution {}
impl Solution {
    pub fn shortest_path_all_keys(grid: Vec<String>) -> i32 {
        
    }
}

fn main() {
  assert_eq!(0, Solution::shortest_path_all_keys(0));
  println!("Pass test cases!");
}
