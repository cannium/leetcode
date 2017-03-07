package main

import "fmt"

func firstMissingPositive(nums []int) int {
	for i := 0; i < len(nums); i++ {
		n := nums[i]
		for n > 0 && n <= len(nums) && n != i+1 && nums[i] != nums[n-1] {
			nums[i], nums[n-1] = nums[n-1], nums[i]
			n = nums[i]
		}
	}
	for i := 0; i < len(nums); i++ {
		if nums[i] != i+1 {
			return i + 1
		}
	}
	return len(nums) + 1
}
