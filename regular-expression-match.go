package main

import (
	"fmt"
)

func getToken(p []byte) (token []byte, pRemain []byte) {
	if len(p) == 0 {
		return
	}
	if len(p) == 1 {
		return p[0:1], pRemain
	}
	if p[1] == '*' {
		return p[:2], p[2:]
	} else {
		return p[0:1], p[1:]
	}
}

func isMatch(s string, p string) bool {
	token, pRemain := getToken([]byte(p))
	return match([]byte(s), token, pRemain)
}

func matchByte(s byte, token byte) bool {
	switch token {
	case '.':
		return true
	default:
		if s == token {
			return true
		} else {
			return false
		}
	}
}

func match(s []byte, token []byte, pRemain []byte) bool {
	if len(token) == 0 {
		if len(s) == 0 {
			return true
		} else {
			return false
		}
	}
	if len(token) == 1 {
		if len(s) == 0 {
			return false
		}
		if !matchByte(s[0], token[0]) {
			return false
		}
		token, pRemain = getToken(pRemain)
		return match(s[1:], token, pRemain)
	}
	// len(token) == 2, i.e. .*
	nextToken, nextP := getToken(pRemain)
	if len(s) == 0 {
		return match(s, nextToken, nextP)
	}
	if matchByte(s[0], token[0]) {
		return match(s[1:], token, pRemain) ||
			match(s, nextToken, nextP)
	} else {
		return match(s, nextToken, nextP)
	}
}

func main() {
	p := []byte("ab*c.de.*")
	for {
		token, remain := getToken(p)
		fmt.Println(string(token), "|", string(remain))
		if len(remain) == 0 {
			break
		}
		p = remain
	}
	fmt.Println(isMatch("aa", "a"))
	fmt.Println(isMatch("aa", "aa"))
	fmt.Println(isMatch("aaa", "aa"))
	fmt.Println(isMatch("aa", "a*"))
	fmt.Println(isMatch("aa", ".*"))
	fmt.Println(isMatch("ab", ".*"))
	fmt.Println(isMatch("aab", "c*a*b"))

	fmt.Println(isMatch("xyza", ".*ab.*"))
	fmt.Println(isMatch("xxabcd", ".*ab.*"))
	fmt.Println(isMatch("bbbbba", ".*a*a"))
}
