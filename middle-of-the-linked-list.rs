// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}

struct Solution {}

impl Solution {
    pub fn middle_node(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut p1 = head.as_ref();
        let mut p2 = head.as_ref();
        loop {
            p1 = Self::one_step(p1);
            if p1 == None {
                match p2 {
                    Some(node) => {
                        return Some(node.clone())
                    }
                    None => {
                        return None
                    }
                }
            }
            p1 = Self::one_step(p1);
            p2 = Self::one_step(p2);
        }
    }
    fn one_step(p: Option<&Box<ListNode>>) -> Option<&Box<ListNode>> {
        match p {
            Some(node) => {
                match &node.next {
                    Some(next) => Some(&next),
                    None => None
                }
            },
            None => None
        }
    }
} 

fn main() {
    let n1 = Some(Box::new(ListNode{
        val: 1,
        next: Some(Box::new(ListNode{
            val: 2,
            next: Some(Box::new(ListNode{
                val: 3,
                next: Some(Box::new(ListNode{
                    val: 4,
                    next: None,
                }))
            }))
        }))
    }));

    let ans1 = Solution::middle_node(n1);
    print!("{:?}\n", ans1);
}