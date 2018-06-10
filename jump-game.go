package main

import (
	"fmt"
)

func canJump(nums []int) bool {
	visited := make([]bool, len(nums))
	q := make(chan int, len(nums))
	visited[0] = true
	q <- 0

	for len(q) > 0 {
		i := <-q
		maxLen := nums[i]
		if i+maxLen >= len(nums)-1 {
			return true
		}
		for j := i; j <= i+maxLen; j++ {
			if !visited[j] {
				visited[j] = true
				q <- j
			}
		}
	}
	return false
}

func main() {
	fmt.Println(canJump([]int{2, 3, 1, 1, 4}))
	fmt.Println(canJump([]int{3, 2, 1, 0, 4}))
	fmt.Println(canJump([]int{5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0}))
}
