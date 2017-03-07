package main

import "fmt"

func generateParenthesis(n int) []string {
	if n <= 0 {
		return []string{}
	}
	memo := [][]string{
		[]string{"()"},
		[]string{"()()", "(())"},
	}
	if n <= 2 {
		return memo[n-1]
	}
	for k := 3; k <= n; k++ {
		dedup := make(map[string]bool)
		for i := 1; i <= k/2; i++ {
			for _, s1 := range memo[i-1] {
				for _, s2 := range memo[k-i-1] {
					dedup[s1+s2] = true
					dedup[s2+s1] = true
				}
			}
		}
		for _, s := range memo[k-2] {
			dedup["("+s+")"] = true
		}
		ansk := make([]string, 0, len(dedup))
		for k, _ := range dedup {
			ansk = append(ansk, k)
		}
		memo = append(memo, ansk)
	}
	return memo[n-1]
}

func main() {
	fmt.Println(generateParenthesis(3))
	fmt.Println(generateParenthesis(4))
	fmt.Println(generateParenthesis(5))
}
