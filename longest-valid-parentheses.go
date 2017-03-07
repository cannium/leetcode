package main

func longestValidParentheses(s string) int {
	p := -1
	stack := make([]int, 0)
	for i := 0; i < len(s); i++ {
		if s[i] == '(' {
			stack = append(stack, i)
			p++
		} else { // ')'
			if p == -1 || s[stack[p]] != '(' {
				stack = append(stack, i)
				p++
			} else {
				stack = stack[:p]
				p--
			}
		}
	}
	stack = append(stack, len(s))
	fmt.Println(stack)
	longest := 0
	lastUnmatch := -1
	for i := 0; i < len(stack); i++ {
		x := stack[i] - lastUnmatch - 1
		if x > longest {
			longest = x
		}
		lastUnmatch = stack[i]
	}
	return longest
}
