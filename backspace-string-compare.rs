use std::iter::FromIterator;

struct Solution{}

impl Solution {
    pub fn backspace_compare(s: String, t: String) -> bool {
        Self::simulate(s) == Self::simulate(t)
    }
    fn simulate(s: String) -> String {
        let mut result = Vec::new();
        for c in s.chars() {
            if c == '#' {
                result.pop();
            } else {
                result.push(c);
            }
        }
        String::from_iter(result)
    }
}

fn main() {
    println!("{:?}", 
    Solution::backspace_compare("a##c".to_string(), "#a#c".to_string()));
}