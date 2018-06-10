package main

import "fmt"

func shiftingLetters(S string, shifts []int) string {
	if len(shifts) == 0 {
		return S
	}
	sum := 0
	for i := len(shifts) - 1; i >= 0; i-- {
		nextSum := sum + shifts[i]
		shifts[i] = (shifts[i] + sum) % 26
		sum = nextSum
		//fmt.Println(i, sum, shifts)
	}
	ss := []byte(S)
	for i := range ss {
		s := (int(ss[i])-int('a')+shifts[i])%26 + int('a')
		ss[i] = byte(s)
	}
	return string(ss)
}

func main() {
	fmt.Println(shiftingLetters("abc", []int{3, 5, 9}))
	fmt.Println(shiftingLetters("abc", []int{26, 26, 26}))
}
