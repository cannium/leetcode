package main

import "fmt"

func findSubstring(s string, words []string) []int {
	var ans []int
	if len(s) == 0 {
		return ans
	}
	if len(words) == 0 {
		return ans
	}
	all := make(map[string]int)
	for _, w := range words {
		if count, ok := all[w]; ok {
			all[w] = count + 1
		} else {
			all[w] = 1
		}
	}
	//fmt.Println("all", all)
	wLen := len(words[0])
	totalLen := len(words) * wLen
	memo := make(map[string]int)
	foundCount := 0
	for i := 0; i <= len(s)-wLen; {
		//fmt.Println(i, memo)
		w := s[i : i+wLen]
		if _, found := all[w]; found {
			foundCount += 1
			i += wLen
			if count, ok := memo[w]; ok {
				if count == all[w] {
					i = i - foundCount*wLen + 1
					foundCount = 0
					memo = make(map[string]int)
				} else {
					memo[w] = count + 1
				}
			} else { // no memo
				memo[w] = 1
			}
			if foundCount == len(words) {
				ans = append(ans, i-totalLen)
				memo = make(map[string]int)
				i = i - totalLen + 1
				foundCount = 0
			}
		} else { // not found
			i = i - foundCount*wLen + 1
			memo = make(map[string]int)
			foundCount = 0
		}
	}
	return ans
}

func main() {
	fmt.Println(findSubstring("barfoothefoobarman", []string{"foo", "bar"}))
	fmt.Println(findSubstring("barfoofoobarthefoobarman",
		[]string{"foo", "bar", "the"}))
	fmt.Println(findSubstring("wordgoodgoodgoodbestword",
		[]string{"word", "good", "best", "good"}))
	fmt.Println(findSubstring("aabbaabbaabb",
		[]string{"bb", "aa", "bb", "aa", "bb"}))
}
