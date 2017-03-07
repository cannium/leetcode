package main

import "fmt"

func removeElement(nums []int, val int) int {
	if len(nums) == 0 {
		return 0
	}
	p := 0
	for i := range nums {
		if nums[i] != val {
			nums[p] = nums[i]
			p++
		}
	}
	return p
}

func main() {
	fmt.Println(removeElement([]int{1, 2, 3, 4, 5, 5}, 3))
}
