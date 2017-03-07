package main

import "fmt"

func myAtoi(str string) int {
	for len(str) > 0 && str[0] == ' ' {
		str = str[1:]
	}

	if len(str) == 0 {
		return 0
	}

	negtive := false
	if str[0] == '-' || str[0] == '+' {
		if str[0] == '-' {
			negtive = true
		}
		str = str[1:]
	}

	var ans int32
	overflow := false
	for i := 0; i < len(str); i++ {
		if str[i] >= '0' && str[i] <= '9' {
			if ans > 2147483647/10 {
				overflow = true
				break
			}
			var digit int32
			digit = int32(str[i] - '0')
			ans = ans*10 + digit
			fmt.Println(digit, ans)
			if ans < 0 {
				overflow = true
				break
			}
		} else {
			break
		}
	}
	if negtive {
		ans = -ans
		if overflow {
			ans = -2147483648
		}
		return int(ans)
	} else {
		if overflow {
			ans = 2147483647
		}
		return int(ans)
	}
}

func main() {
	/*
		fmt.Println(myAtoi(""))
		fmt.Println(myAtoi("12345aaa"))
		fmt.Println(myAtoi("+-2"))
		fmt.Println(myAtoi("9223372036854775809"))
	*/
	//fmt.Println(myAtoi("1095502006p8"))
	//fmt.Println(myAtoi("18446744073709551617"))
	fmt.Println(myAtoi("    10522545459"))
}
