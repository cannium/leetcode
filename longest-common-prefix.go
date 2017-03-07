package main

import "fmt"

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}
	i := 0
Outer:
	for {
		var w byte
		for _, s := range strs {
			if len(s) < i+1 {
				break Outer
			}
			if w == 0 {
				w = s[i]
			} else {
				if w != s[i] {
					break Outer
				}
			}
		}
		i += 1
	}
	return strs[0][:i]
}

func main() {
	fmt.Println(longestCommonPrefix([]string{
		"abc",
		"abd",
		"abd"}))
}
