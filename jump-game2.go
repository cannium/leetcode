package main

import (
	"fmt"
)

func jump(nums []int) int {
	if len(nums) <= 1 {
		return 0
	}
    visited := make([]bool, len(nums))
	q := make(chan int, len(nums))
	step := make(chan int, len(nums))
    visited[0] = true
	q <- 0
	step <- 0

    for len(q) > 0 {
		i := <- q
		s := <- step
		fmt.Println(i, s)
        maxLen := nums[i]
        for j := i + 1; j <= i + maxLen; j++ {
			if j >= len(nums) - 1 {
				return s + 1
			}
            if !visited[j] {
                visited[j] = true
				q <- j
				step <- (s + 1)
            }
        }
    }
    return -1
}

func main() {
	fmt.Println(jump([]int{2,3,1,1,4}))
	fmt.Println(jump([]int{1,2,1,1,1}))
	fmt.Println(jump([]int{1,2}))
}