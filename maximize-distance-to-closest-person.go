package main

import "fmt"

func maxDistToClosest(seats []int) int {
	longest := 0
	this := 0
	last := -1
	for i := range seats {
		//fmt.Println(this, last,longest)
		if seats[i] == 0 {
			this += 1
			continue
		}
		if seats[i] == 1 {
			if last == -1 {
				longest = this
			} else {
				if (this+1)/2 > longest {
					longest = (this + 1) / 2
				}
			}
			this = 0
			last = i
		}
	}

	if this > longest {
		longest = this
	}
	return longest
}

func main() {
	fmt.Println(maxDistToClosest([]int{1, 0, 0, 0, 1, 0, 1}))
	fmt.Println(maxDistToClosest([]int{1, 0, 0, 0}))
	fmt.Println(maxDistToClosest([]int{0, 0, 0, 1}))
	fmt.Println(maxDistToClosest([]int{0, 0, 0, 0, 1, 1, 0, 0, 0}))
}
