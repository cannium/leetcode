struct MinStack {
    stack: Vec<(i32, usize)>
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {

    /** initialize your data structure here. */
    fn new() -> Self {
        MinStack{
            stack: Vec::new()
        }
    }
    
    fn push(&mut self, x: i32) {
        if self.stack.len() == 0 {
            self.stack.push((x, 0));
            return;
        }
        let &(_, min_i) = self.stack.last().unwrap();
        if self.stack[min_i].0 < x {
            self.stack.push((x, min_i.clone()));
        } else {
            self.stack.push((x, self.stack.len()));
        }
    }
    
    fn pop(&mut self) {
        self.stack.pop();
    }
    
    fn top(&self) -> i32 {
        match self.stack.last() {
            Some(&(x, _)) => x.clone(),
            None => 0
        }
    }
    
    fn get_min(&self) -> i32 {
        match self.stack.last() {
            Some(&(_, i)) => self.stack[i].0.clone(),
            None => 0
        }
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * let obj = MinStack::new();
 * obj.push(x);
 * obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: i32 = obj.get_min();
 */

 fn main() {
    let mut obj = MinStack::new();
    obj.push(-2);
    obj.push(0);
    obj.push(-3);
    println!("{:?}", obj.get_min());
    obj.pop();
    println!("{:?}", obj.top());
    println!("{:?}", obj.get_min());
 }