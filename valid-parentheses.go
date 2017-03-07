package main

import "fmt"

func isValid(s string) bool {
	stack := make([]byte, 0)
	p := -1
	pair := map[byte]byte{
		'}': '{',
		']': '[',
		')': '(',
	}
	for i, _ := range s {
		w := s[i]
		switch w {
		case '{', '(', '[':
			stack = append(stack, w)
			p += 1
		case '}', ')', ']':
			if len(stack) == 0 {
				return false
			}
			if stack[p] == pair[w] {
				stack = stack[:len(stack)-1]
				p -= 1
			} else {
				return false
			}
		}
	}
	if len(stack) == 0 {
		return true
	} else {
		return false
	}
}

func main() {
	fmt.Println(isValid("()[]{}"))
	fmt.Println(isValid("(((())))"))
	fmt.Println(isValid("[{}()]"))
	fmt.Println(isValid("{]"))
}
