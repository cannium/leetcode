package main

import (
	"fmt"
)

func reverse(x int) int {
	arr := make([]int, 0)
	negtive := false
	if x < 0 {
		x = -x
		negtive = true
	}
	for x != 0 {
		m := x % 10
		x = x / 10
		arr = append(arr, m)
	}
	ans := 0
	for i := 0; i < len(arr); i++ {
		ans = ans*10 + arr[i]
	}
	if ans > 1<<31-1 {
		return 0
	}
	if negtive {
		return -ans
	} else {
		return ans
	}
}

func main() {
	fmt.Println(reverse(123))
	fmt.Println(reverse(-123))
	fmt.Println(reverse(-100))
	fmt.Println(reverse(1000000003))
	fmt.Println(reverse(1534236469))
}
