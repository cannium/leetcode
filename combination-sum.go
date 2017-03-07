package main

import "fmt"
import "sort"

func try(ans *[][]int, now []int, sumNow int, candidates []int, target int) {
	if sumNow == target {
		copied := make([]int, len(now))
		copy(copied, now)
		*ans = append(*ans, copied)
		return
	}
	for _, x := range candidates {
		if len(now) != 0 && x < now[len(now)-1] {
			continue
		}
		if sumNow+x > target {
			return
		}
		now = append(now, x)
		try(ans, now, sumNow+x, candidates, target)
		now = now[:len(now)-1]
	}
}

func combinationSum(candidates []int, target int) [][]int {
	ans := make([][]int, 0)
	if len(candidates) == 0 {
		return ans
	}
	sort.Ints(candidates)
	try(&ans, make([]int, 0), 0, candidates, target)
	return ans
}

func main() {
	fmt.Println(combinationSum([]int{2, 3, 6, 7}, 7))
}
