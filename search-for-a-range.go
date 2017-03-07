package main

func search(nums []int, target, start, end int) []int {
	if start > end {
		return []int{-1, -1}
	}
	if nums[start] > target || nums[end] < target {
		return []int{-1, -1}
	}
	if start == end {
		if nums[start] == target {
			return []int{start, start}
		} else {
			return []int{-1, -1}
		}
	}
	mid := (start + end) / 2
	if nums[mid] == target {
		left := mid
		right := mid
		l := search(nums, target, start, mid-1)
		if l[0] != -1 {
			left = l[0]
		}
		r := search(nums, target, mid+1, end)
		if r[1] != -1 {
			right = r[1]
		}
		return []int{left, right}
	}
	if nums[mid] > target {
		return search(nums, target, start, mid-1)
	} else {
		return search(nums, target, mid+1, end)
	}
}

func searchRange(nums []int, target int) []int {
	if len(nums) == 0 {
		return []int{-1, -1}
	}
	return search(nums, target, 0, len(nums)-1)
}
