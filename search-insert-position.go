package main

func findPos(nums []int, target, start, end int) int {
	if start == end {
		if nums[start] == target {
			return start
		}
		if nums[start] > target {
			return start
		} else {
			return start + 1
		}
	}
	if nums[start] > target {
		return start
	}
	if nums[end] < target {
		return end + 1
	}

	mid := (start + end) / 2
	if nums[mid] == target {
		return mid
	}
	if nums[mid] > target {
		return findPos(nums, target, start, mid-1)
	} else {
		return findPos(nums, target, mid+1, end)
	}
}

func searchInsert(nums []int, target int) int {
	if len(nums) == 0 {
		return 0
	}
	return findPos(nums, target, 0, len(nums)-1)
}
