package main

import "fmt"

import "sort"

type slices [][]int

func (s slices) Len() int {
	return len(s)
}

func (s slices) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func (s slices) Less(i, j int) bool {
	if len(s[i]) < len(s[j]) {
		return true
	}
	if len(s[i]) > len(s[j]) {
		return false
	}
	for k := 0; k < len(s[i]); k++ {
		if s[i][k] == s[j][k] {
			continue
		}
		if s[i][k] < s[j][k] {
			return true
		}
		return false
	}
	return false
}

func try(ans *[][]int, candidates []int, current []int,
	target, sumNow, cursor int) {

	if sumNow == target {
		copied := make([]int, len(current))
		copy(copied, current)
		sort.Ints(copied)
		*ans = append(*ans, copied)
		return
	}
	if sumNow > target {
		return
	}
	for i := cursor; i < len(candidates); i++ {
		current = append(current, candidates[i])
		try(ans, candidates, current, target, sumNow+candidates[i], i+1)
		current = current[:len(current)-1]
	}
}

func eq(a, b []int) bool {
	if len(a) != len(b) {
		return false
	}
	for i := 0; i < len(a); i++ {
		if a[i] != b[i] {
			return false
		}
	}
	return true
}

func combinationSum2(candidates []int, target int) [][]int {
	ans := make([][]int, 0)
	if len(candidates) == 0 {
		return ans
	}
	try(&ans, candidates, []int{}, target, 0, 0)
	sort.Sort(slices(ans))
	out := make([][]int, 0)
	var last []int
	for i := 0; i < len(ans); i++ {
		if !eq(ans[i], last) {
			out = append(out, ans[i])
		}
		last = ans[i]
	}
	return out
}

func main() {
	ans := combinationSum2([]int{10, 1, 2, 7, 6, 1, 5}, 8)
	fmt.Println(ans)
}
