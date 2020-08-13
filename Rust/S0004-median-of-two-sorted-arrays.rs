//There are two sorted arrays nums1 and nums2 of size m and n respectively.
// Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
// You may assume nums1 and nums2 cannot be both empty.
//
// Example 1:
//nums1 = [1, 3]
//nums2 = [2]
//
//The median is 2.0
// Example 2:
//nums1 = [1, 2]
//nums2 = [3, 4]
//
//The median is (2 + 3)/2 = 2.5
pub struct Solution {}

impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        let (mut nums1, mut nums2) = (nums1, nums2);
        if nums1.len() > nums2.len() {
            std::mem::swap(&mut nums1, &mut nums2);
        }

        let (n, m) = (nums1.len(), nums2.len());
        let (mut low, mut high, target) = (0, n, (n+m+1)/2);
        loop {
            let partition1_loc = (low + high) / 2;
            let partition2_loc = target - partition1_loc;

            let partition1_left_max = if partition1_loc == 0 {
                std::i32::MIN
            } else {
                nums1[partition1_loc-1]
            };
            let partition1_right_min = if partition1_loc == n {
                std::i32::MAX
            } else {
                nums1[partition1_loc]
            };

            let partition2_left_max = if partition2_loc == 0 {
                std::i32::MIN
            } else {
                nums2[partition2_loc-1]
            };
            let partition2_right_min = if partition2_loc == m {
                std::i32::MAX
            } else {
                nums2[partition2_loc]
            };

            if partition1_left_max > partition2_right_min {
                high = partition1_loc - 1;
            } else if partition2_left_max > partition1_right_min{
                low = partition1_loc + 1;
            } else {
                if (n+m) % 2 == 0 {
                    let left_max = partition1_left_max.max(partition2_left_max);
                    let right_min = partition1_right_min.min(partition2_right_min);
                    return (left_max as f64 + right_min as f64) / 2.0;
                } else {
                    return partition1_left_max.max(partition2_left_max) as f64;
                }
            }
        }
    }
}

fn main() {
    assert_eq!(1., Solution::find_median_sorted_arrays(vec![], vec![1]));
    assert_eq!(3., Solution::find_median_sorted_arrays(vec![], vec![1, 3, 5]));
    assert_eq!(1.5, Solution::find_median_sorted_arrays(vec![], vec![1, 2]));
    assert_eq!(1.5, Solution::find_median_sorted_arrays(vec![], vec![0, 1, 2, 3]));
    assert_eq!(-1., Solution::find_median_sorted_arrays(vec![3], vec![-2, -1]));
    assert_eq!(2., Solution::find_median_sorted_arrays(vec![1], vec![2, 3]));
    assert_eq!(7., Solution::find_median_sorted_arrays(vec![2, 7, 11, 15], vec![2, 7, 15]));
    assert_eq!(7., Solution::find_median_sorted_arrays(vec![2, 7, 11, 15], vec![2, 9, 13, 15]));
    assert_eq!(4.5, Solution::find_median_sorted_arrays(vec![2, 7, 11, 15], vec![-2, -1]));
    assert_eq!(2., Solution::find_median_sorted_arrays(vec![2, 7, 11, 15], vec![-5, -2, -1]));
    assert_eq!(2., Solution::find_median_sorted_arrays(vec![1, 3], vec![2]));
    assert_eq!(2.5, Solution::find_median_sorted_arrays(vec![1, 2], vec![3, 4]));
    println!("Pass test cases!");
}

