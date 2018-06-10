package main

import "fmt"

var memo map[int][]int

func calc(graph map[int][]int,
	quiet []int, i int) (rNode int, rQuiet int) {

	if pair, ok := memo[i]; ok {
		return pair[0], pair[1]
	}

	rNode = i
	rQuiet = quiet[i]
	for _, node := range graph[i] {
		n, q := calc(graph, quiet, node)
		if q < rQuiet {
			rNode = n
			rQuiet = q
		}
	}
	memo[i] = []int{rNode, rQuiet}
	return
}

func loudAndRich(richer [][]int, quiet []int) []int {
	Richer := make(map[int][]int)
	memo = make(map[int][]int)
	for _, pair := range richer {
		rich := pair[0]
		poor := pair[1]
		Richer[poor] = append(Richer[poor], rich)
	}
	//fmt.Println(Richer)
	answer := make([]int, len(quiet))
	for i := range answer {
		n, _ := calc(Richer, quiet, i)
		answer[i] = n
	}
	return answer
}

func main() {
	fmt.Println(
		loudAndRich([][]int{
			{1, 0}, {2, 1}, {3, 1}, {3, 7}, {4, 3}, {5, 3}, {6, 3},
		}, []int{3, 2, 5, 4, 6, 1, 7, 0}))
}
