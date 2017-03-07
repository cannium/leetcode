package main

import "fmt"

var longest int
var x, y int

func longestPalindrome(s string) string {
	if len(s) == 1 {
		return s
	}
	longest = 0
	x = 0
	y = 0
	for i := 0; i < len(s)-1; i++ {
		expand(s, i, i)
		if s[i] == s[i+1] {
			expand(s, i, i+1)
		}
	}
	return s[x : y+1]
}

func expand(s string, i int, j int) {
	for {
		if i-1 >= 0 && j+1 < len(s) {
			i--
			j++
			if s[i] != s[j] {
				i++
				j--
				break
			}
		} else {
			break
		}
	}
	if j-i+1 > longest {
		longest = j - i + 1
		x = i
		y = j
	}
}

func main() {
	fmt.Println(longestPalindrome("babad"))
	fmt.Println(longestPalindrome("cbbd"))
	fmt.Println(longestPalindrome("abcdefg"))
	fmt.Println(longestPalindrome("aaaaaaaaaaaaaaaaaa"))
	fmt.Println(longestPalindrome("aaabaaaa"))
}
