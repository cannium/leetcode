use std::collections::HashMap;

impl Solution {
    pub fn count_elements(arr: Vec<i32>) -> i32 {
        let mut m : HashMap<i32, bool> = HashMap::new();
        for n in arr.iter() {
            m.insert(*n, true);
        }
        let mut ans = 0;
        for n in arr.iter() {
            if m.contains_key(&(n+1)) {
                ans += 1;
            }
        }
        return ans;
    }
}
