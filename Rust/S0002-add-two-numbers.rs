/*
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
*/
pub struct Solution {}

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>
}
//
impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode {
            next: None,
            val
        }
    }
}

// helper function for test
pub fn to_list(vec: Vec<i32>) -> Option<Box<ListNode>> {
    let mut current = None;
    for &v in vec.iter().rev() {
        let mut node = ListNode::new(v);
        node.next = current;
        current = Some(Box::new(node));
    }
    current
}

impl Solution {
    pub fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let (mut p, mut q) = (l1, l2);
        let mut dummy_head = Some(Box::new(ListNode::new(0)));
        let mut current = dummy_head.as_mut();
        let mut overflow = false;
        loop {
            let mut node_val = if overflow {1} else {0};
            if let Some(node) = p {
                node_val += node.val;
                p = node.next;
            };
            if let Some(node) = q {
                node_val += node.val;
                q = node.next;
            };
            let node_val = if node_val >= 10 {
                overflow = true;
                node_val - 10
            } else {
                overflow = false;
                node_val
            };
            current.as_mut().unwrap().next = Some(Box::new(ListNode::new(node_val)));
            current = &mut current.as_mut().unwrap().next;
            if !p.is_some() && !q.is_some() && !overflow {
                break dummy_head.unwrap().next;
            }
        }
    }
}

fn main() {
    assert_eq!(
        from_vec(vec![7, 0, 8]),
        Solution::add_two_numbers(from_vec(vec![2, 4, 3]), from_vec(vec![5, 6, 4]))
    );

    assert_eq!(
        from_vec(vec![7, 0, 1]),
        Solution::add_two_numbers(from_vec(vec![3, 4]), from_vec(vec![4, 6]))
    );

    assert_eq!(
        from_vec(vec![8, 9, 9, 9, 0, 0, 1]),
        Solution::add_two_numbers(from_vec(vec![9, 9, 9, 9]), from_vec(vec![9, 9, 9, 9, 9, 9]))
    );

    assert_eq!(
        from_vec(vec![0]),
        Solution::add_two_numbers(from_vec(vec![0]), from_vec(vec![0]))
    );
    println!("Pass test cases!");
}

