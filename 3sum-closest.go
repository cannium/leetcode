package main

import (
	"fmt"
	"sort"
)

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func threeSumClosest(nums []int, target int) int {
	sort.Ints(nums)
	closest := nums[0] + nums[1] + nums[2]
	for i := 1; i < len(nums)-1; i++ {
		l := i - 1
		r := i + 1
		for {
			now := nums[l] + nums[r] + nums[i]
			if now == target {
				return target
			}
			if abs(now-target) < abs(closest-target) {
				closest = now
			}
			if now > target {
				l--
			} else {
				r++
			}
			if l < 0 || r >= len(nums) {
				break
			}
		}
	}
	return closest
}

func main() {
	fmt.Println(threeSumClosest([]int{-1, 2, 1, -4}, 1))
}
