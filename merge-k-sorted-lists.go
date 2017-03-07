package main

import "fmt"

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	}
	if l2 == nil {
		return l1
	}
	var out, p *ListNode
	if l1.Val < l2.Val {
		out = l1
		l1 = l1.Next
	} else {
		out = l2
		l2 = l2.Next
	}
	p = out
	for l1 != nil && l2 != nil {
		if l1.Val < l2.Val {
			p.Next = l1
			l1 = l1.Next
		} else {
			p.Next = l2
			l2 = l2.Next
		}
		p = p.Next
	}
	if l1 == nil {
		p.Next = l2
	} else {
		p.Next = l1
	}
	return out
}

func mergeKLists(lists []*ListNode) *ListNode {
	if len(lists) == 0 {
		return nil
	}
	for len(lists) > 1 {
		c := mergeTwoLists(lists[0], lists[1])
		lists = lists[2:]
		lists = append(lists, c)
	}
	return lists[0]
}

func buildList(arr []int) *ListNode {
	head := &ListNode{
		Val:  arr[0],
		Next: nil,
	}
	p := head
	for i := 1; i < len(arr); i++ {
		p.Next = &ListNode{
			Val:  arr[i],
			Next: nil,
		}
		p = p.Next
	}
	return head
}

func main() {
	ans := mergeKLists([]*ListNode{
		buildList([]int{1, 3, 7}),
		buildList([]int{2, 9, 10}),
		buildList([]int{1, 2, 3}),
	})
	for {
		if ans == nil {
			break
		}
		fmt.Println(ans.Val)
		ans = ans.Next
	}
}
