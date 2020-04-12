struct Solution{}

use std::collections::BinaryHeap;

impl Solution {
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        let mut heap = BinaryHeap::new();
        for i in stones.iter() {
            heap.push(*i);
        }
        while heap.len() > 1 {
            let mut x = heap.pop().unwrap();
            let mut y = heap.pop().unwrap();
            if x > y {
                std::mem::swap(&mut x, &mut y);
            }
            if x == y {
                continue;
            }
            let new = y-x;
            heap.push(new);
        }
        if heap.len() == 0 {
            return 0;
        }
        return heap.pop().unwrap();
    }
}

fn main() {
    println!("{:?}", Solution::last_stone_weight(vec![2,7,4,1,8,1]));
}