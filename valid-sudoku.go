package main

func isValid9(arr []byte) bool {
	fmt.Println(string(arr))
	memo := make(map[byte]bool)
	for _, b := range arr {
		if b == '.' {
			continue
		}
		if _, ok := memo[b]; ok {
			return false
		} else {
			memo[b] = true
		}
	}
	return true
}

func isValidSudoku(board [][]byte) bool {
	for i := 0; i < 9; i++ {
		if !isValid9(board[i]) {
			return false
		}
	}
	for i := 0; i < 9; i++ {
		arr := make([]byte, 9)
		for j := 0; j < 9; j++ {
			arr[j] = board[j][i]
		}
		if !isValid9(arr) {
			return false
		}
	}
	base := [][]int{
		[]int{0, 0},
		[]int{0, 3},
		[]int{0, 6},
		[]int{3, 0},
		[]int{3, 3},
		[]int{3, 6},
		[]int{6, 0},
		[]int{6, 3},
		[]int{6, 6},
	}
	shift := [][]int{
		[]int{0, 0},
		[]int{0, 1},
		[]int{0, 2},
		[]int{1, 0},
		[]int{1, 1},
		[]int{1, 2},
		[]int{2, 0},
		[]int{2, 1},
		[]int{2, 2},
	}
	for _, b := range base {
		arr := make([]byte, 0)
		for _, s := range shift {
			i := b[0] + s[0]
			j := b[1] + s[1]
			arr = append(arr, board[i][j])
		}
		if !isValid9(arr) {
			return false
		}
	}
	return true
}
