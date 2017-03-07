package main

func strStr(haystack string, needle string) int {
	if len(haystack) < len(needle) {
		return -1
	}
	for i := 0; i <= len(haystack)-len(needle); i++ {
		same := true
		for j := range needle {
			if haystack[i+j] != needle[j] {
				same = false
				break
			}
		}
		if same {
			return i
		}
	}
	return -1
}
