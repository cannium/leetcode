package main

import "fmt"

type Memo map[byte]bool

func toBlock(x, y int) int {
	return (x/3)*3 + y/3
}

func fill(board [][]byte, lineMemo, columnMemo, blockMemo []Memo,
	startX, startY int) bool {

	for i := startX; i < 9; i++ {
		var j int
		if i == startX {
			j = startY
		} else {
			j = 0
		}
		for ; j < 9; j++ {
			if board[i][j] != '.' {
				continue
			}
			for n := byte('1'); n <= byte('9'); n++ {
				_, okLine := lineMemo[i][n]
				_, okColumn := columnMemo[j][n]
				_, okBlock := blockMemo[toBlock(i, j)][n]
				if !okLine && !okColumn && !okBlock {
					board[i][j] = n
					lineMemo[i][n] = true
					columnMemo[j][n] = true
					blockMemo[toBlock(i, j)][n] = true

					good := fill(board, lineMemo, columnMemo, blockMemo, i, j)
					if good {
						return true
					}
					board[i][j] = '.'
					delete(lineMemo[i], n)
					delete(columnMemo[j], n)
					delete(blockMemo[toBlock(i, j)], n)
				}
			}
			return false
		}
	}
	return true
}

func solveSudoku(board [][]byte) {
	lineMemo := make([]Memo, 9)
	columnMemo := make([]Memo, 9)
	blockMemo := make([]Memo, 9)
	for i := 0; i < 9; i++ {
		lineMemo[i] = make(Memo)
		columnMemo[i] = make(Memo)
		blockMemo[i] = make(Memo)
	}
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			x := board[i][j]
			if x == '.' {
				continue
			}
			lineMemo[i][x] = true
			columnMemo[j][x] = true
			blockMemo[toBlock(i, j)][x] = true
		}
	}
	fill(board, lineMemo, columnMemo, blockMemo, 0, 0)
}

func main() {

	x := [][]byte{
		[]byte("..9748..."),
		[]byte("7........"),
		[]byte(".2.1.9..."),
		[]byte("..7...24."),
		[]byte(".64.1.59."),
		[]byte(".98...3.."),
		[]byte("...8.3.2."),
		[]byte("........6"),
		[]byte("...2759..")}
	solveSudoku(x)
	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			fmt.Printf("%s", string(x[i][j]))
		}
		fmt.Printf("\n")
	}
	fmt.Println(isValidSudoku(x))
}

func isValid9(arr []byte) bool {
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
