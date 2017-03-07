package main

import "fmt"

type sm2 struct {
	a int
	b int
}

func uniq(a, b, c int) (k sm2, v int) {
	for {
		changed := false
		if a > b {
			a, b = b, a
			changed = true
		}
		if b > c {
			b, c = c, b
			changed = true
		}
		if a > c {
			a, c = c, a
			changed = true
		}
		if !changed {
			break
		}
	}
	k.a = a
	k.b = b
	v = c
	return
}

func threeSum(nums []int) [][]int {
	m := make(map[int]int)
	for i, n := range nums {
		m[n] = i
	}
	m2 := make(map[sm2]int)
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			need := 0 - nums[i] - nums[j]
			if idx, ok := m[need]; ok && idx > j {
				k, v := uniq(nums[i], nums[j], nums[idx])
				m2[k] = v
			}
		}
	}
	ans := make([][]int, 0, len(m2))
	for k, v := range m2 {
		one := []int{k.a, k.b, v}
		ans = append(ans, one)
	}
	return ans
}

func main() {
	fmt.Println(threeSum([]int{-1, 0, 1, 2, -1, -4}))
}
