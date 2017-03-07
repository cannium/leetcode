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

func swapPairs(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	dummy := &ListNode{
		Next: head,
	}
	p := dummy
	for {
		a := p.Next
		b := a.Next
		if b == nil {
			break
		}
		p.Next = b
		a.Next = b.Next
		b.Next = a
		p = p.Next.Next
		if p.Next == nil {
			break
		}
	}
	return dummy.Next
}
