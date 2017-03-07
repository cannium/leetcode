package main

import "fmt"

func countAndSay(n int) string {
	if n == 1 {
		return "1"
	}
	ans := "1"
	for i := 1; i < n; i++ {
		var next string
		var last byte
		count := 0
		for j := range ans {
			b := ans[j]
			if last == 0 {
				last = b
				count = 1
				continue
			}
			if last == b {
				count++
			} else {
				next += string(count+'0') + string(last)
				last = b
				count = 1
			}
		}
		next += string(count+'0') + string(last)
		ans = next
	}
	return ans
}

func main() {
	fmt.Println(countAndSay(1))
	fmt.Println(countAndSay(2))
	fmt.Println(countAndSay(3))
	fmt.Println(countAndSay(4))
	fmt.Println(countAndSay(5))
	fmt.Println(countAndSay(6))
	fmt.Println(countAndSay(7))
}
