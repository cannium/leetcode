package main

import "fmt"

func convert(s string, numRows int) string {
	if numRows == 1 {
		return s
	}
	arr := make([]string, numRows)
	for i := 0; i < len(s); i++ {
		j := i % (numRows + numRows - 2)
		if j < numRows {
			arr[j] = arr[j] + string(s[i])
		} else {
			k := numRows - (j + 1 - numRows) - 1
			arr[k] = arr[k] + string(s[i])
		}
	}
	ans := ""
	for i := 0; i < numRows; i++ {
		ans = ans + arr[i]
	}
	return ans
}

func main() {
	fmt.Println(convert("PAYPALISHIRING", 1))
	fmt.Println(convert("PAYPALISHIRING", 2))
	fmt.Println(convert("PAYPALISHIRING", 3))
	fmt.Println(convert("PAYPALISHIRING", 4))
}
