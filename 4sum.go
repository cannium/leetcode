package main

import "fmt"
import "sort"

type pair struct {
	x int
	y int
}

type triplet struct {
	x int
	y int
	z int
}

func fourSum(nums []int, target int) [][]int {
	ans := make([][]int, 0)
	m := make(map[int][]pair)
	if len(nums) < 4 {
		return ans
	}
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			sum := nums[i] + nums[j]
			p := pair{
				x: i,
				y: j,
			}
			if pairs, ok := m[sum]; ok {
				m[sum] = append(pairs, p)
			} else {
				m[sum] = []pair{p}
			}
		}
	}
	tri := make(map[triplet]int)
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			need := target - nums[i] - nums[j]
			if pairs, ok := m[need]; ok {
				for _, pp := range pairs {
					if pp.x != i && pp.y != i &&
						pp.x != j && pp.y != j {
						arr := make([]int, 4)
						arr[0] = nums[i]
						arr[1] = nums[j]
						arr[2] = nums[pp.x]
						arr[3] = nums[pp.y]
						sort.Ints(arr)
						t := triplet{
							x: arr[0],
							y: arr[1],
							z: arr[2],
						}
						tri[t] = arr[3]
					}
				}
			}
		}
	}
	for k, v := range tri {
		ans = append(ans, []int{k.x, k.y, k.z, v})
	}
	return ans
}

func main() {
	//fmt.Println(fourSum([]int{1, 0, -1, 0, -2, 2}, 0))
	fmt.Println(fourSum([]int{-3, -2, -1, 0, 0, 1, 2, 3}, 0))
}
