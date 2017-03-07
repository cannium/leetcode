package main

import (
	"fmt"
	"strconv"
)

func isPalindrome(x int) bool {
	xs := strconv.Itoa(x)
	for i := range xs {
		if xs[i] != xs[len(xs)-i-1] {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(isPalindrome(333))
	fmt.Println(isPalindrome(123))
	fmt.Println(isPalindrome(121))
}
