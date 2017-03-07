package main

import "fmt"

func min(x, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}

func maxArea(height []int) int {
	i := 0
	j := len(height) - 1
	max := 0
	for i < j {
		next := min(height[i], height[j]) * (j - i)
		if next > max {
			max = next
		}
		if height[i] > height[j] {
			j--
		} else {
			i++
		}
	}
	return max
}

func main() {
	fmt.Println(maxArea([]int{1, 2, 3, 4}))
}
