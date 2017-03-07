package main

import "fmt"

func fill(height []int, left, right int) int {
	if left >= right {
		return 0
	}
	watermark := height[left]
	if height[left] > height[right] {
		watermark = height[right]
	}
	count := 0
	for i := left + 1; i <= right-1; i++ {
		if height[i] < watermark {
			count += watermark - height[i]
			height[i] = watermark
		}
	}
	return count
}

func trap(height []int) int {
	if len(height) <= 2 {
		return 0
	}
	count := 0
	for {
		changed := false
		left := -1
		right := -1
		for i := 1; i < len(height)-1; i++ {
			if height[i] < height[i-1] {
				if left != -1 && right != -1 {
					filled := fill(height, left, right)
					if filled > 0 {
						count += filled
						changed = true
					}
					left = -1
					right = -1
				}
				if left == -1 {
					left = i - 1
				}
			}
			if height[i] < height[i+1] {
				right = i + 1
			}
		}
		if left != -1 && right != -1 {
			filled := fill(height, left, right)
			if filled > 0 {
				count += filled
				changed = true
			}
		}
		if !changed {
			break
		}
	}
	return count
}

func main() {
	fmt.Println(trap([]int{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}))
}
