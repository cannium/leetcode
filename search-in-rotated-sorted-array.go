package main

import "fmt"

func searchRange(nums []int, target, start, end int) int {
	if start > end {
		return -1
	}
	if start == end {
		if nums[start] == target {
			return start
		} else {
			return -1
		}
	}
	if nums[start] < nums[end] {
		if nums[start] > target || nums[end] < target {
			return -1
		}
		mid := (start + end) / 2
		if nums[mid] == target {
			return mid
		}
		if nums[mid] > target {
			return searchRange(nums, target, start, mid-1)
		} else {
			return searchRange(nums, target, mid+1, end)
		}
	}

	mid := (start + end) / 2
	if i := searchRange(nums, target, start, mid); i != -1 {
		return i
	} else {
		return searchRange(nums, target, mid+1, end)
	}
}

func search(nums []int, target int) int {
	if len(nums) == 0 {
		return -1
	}
	return searchRange(nums, target, 0, len(nums)-1)
}

func main() {
	fmt.Println(search([]int{4, 5, 6, 7, 0, 1}, 0))
	fmt.Println(search([]int{4, 5, 6, 7, 0, 1}, 1))
	fmt.Println(search([]int{4, 5, 6, 7, 0, 1}, 2))
	fmt.Println(search([]int{4, 5, 6, 7, 0, 1}, 3))
	fmt.Println(search([]int{4, 5, 6, 7, 0, 1}, 4))
	fmt.Println(search([]int{4, 5, 6, 7, 0, 1}, 5))
	fmt.Println(search([]int{4, 5, 6, 7, 0, 1}, 6))
	fmt.Println(search([]int{4, 5, 6, 7, 0, 1}, 7))
	fmt.Println(search([]int{4, 5, 6, 7, 0, 1}, -7))
	fmt.Println(search([]int{4, 5, 6, 7, 0, 1}, 17))
}
