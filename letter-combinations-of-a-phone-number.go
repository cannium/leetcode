package main

import "fmt"

func letterCombinations(digits string) []string {

	keys := map[byte]string{
		'1': "",
		'2': "abc",
		'3': "def",
		'4': "ghi",
		'5': "jkl",
		'6': "mno",
		'7': "pqrs",
		'8': "tuv",
		'9': "wxyz",
		'0': " ",
	}

	var ans []string
	for di, _ := range digits {
		letters := keys[digits[di]]
		if len(ans) == 0 {
			for li, _ := range letters {
				ans = append(ans, string(letters[li]))
			}
		} else {
			var newAns []string
			for _, s := range ans {
				for li, _ := range letters {
					newAns = append(newAns, s+string(letters[li]))
				}
			}
			ans = newAns
		}
	}
	return ans
}

func main() {
	fmt.Println(letterCombinations("23"))
}
