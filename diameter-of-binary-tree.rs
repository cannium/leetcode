// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
  pub val: i32,
  pub left: Option<Rc<RefCell<TreeNode>>>,
  pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
  #[inline]
  pub fn new(val: i32) -> Self {
    TreeNode {
      val,
      left: None,
      right: None
    }
  }
}

struct Solution{}


use std::rc::Rc;
use std::cell::RefCell;
use std::cmp::max;
impl Solution {
    pub fn diameter_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let (diameter, _depth) = Self::find(&root);
        return diameter;
    }
    fn find(root: &Option<Rc<RefCell<TreeNode>>>) -> (i32, i32) {
        match root{
            Some(node) => {
                let node = node.borrow();
                let (left_diameter, left_depth) = Self::find(&node.left);
                let (right_diameter, right_depth) = Self::find(&node.right);
                let diameter = max(left_diameter, max(right_diameter, left_depth+right_depth));
                let depth = max(left_depth, right_depth) + 1;
                return (diameter, depth);
            },
            None => {
                (0, 0)
            }
        }
    }
}

fn main() {
    let tree = Some(Rc::new(RefCell::new(TreeNode{
        val:1,
        left: Some(Rc::new(RefCell::new(TreeNode{
            val:2,
            left: Some(Rc::new(RefCell::new(TreeNode{
                val: 4,
                left: None,
                right: None,
            }))),
            right: Some(Rc::new(RefCell::new(TreeNode{
                val:5,
                left: None,
                right: None,
            }))),
        }))),
        right: Some(Rc::new(RefCell::new(TreeNode{
            val: 3,
            left: None,
            right: None,
        })))
    })));
    println!("{:?}", Solution::diameter_of_binary_tree(tree));
}