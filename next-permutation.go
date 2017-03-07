package main

import "fmt"

func reverse(nums []int) {
	i := 0
	j := len(nums) - 1
	for i < j {
		nums[i], nums[j] = nums[j], nums[i]
		i++
		j--
	}
}

func np(nums []int) bool {
	if len(nums) == 2 {
		if nums[0] < nums[1] {
			nums[0], nums[1] = nums[1], nums[0]
			return true
		} else {
			return false
		}
	}
	if np(nums[1:]) {
		return true
	}
	// now nums[1:] is in reverse order
	if nums[0] >= nums[1] {
		return false
	}
	reverse(nums[1:])
	for i := 1; i < len(nums); i++ {
		if nums[i] > nums[0] {
			nums[0], nums[i] = nums[i], nums[0]
			return true
		}
	}
	return true
}

func nextPermutation(nums []int) {
	if len(nums) <= 1 {
		return
	}
	if !np(nums) {
		reverse(nums)
	}
}

func main() {
	x := []int{1, 2, 3, 4, 5}
	nextPermutation(x)
	fmt.Println(x)
	reverse(x)
	fmt.Println(x)
	nextPermutation(x)
	fmt.Println(x)
}
