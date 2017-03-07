package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	dummy := &ListNode{
		Next: head,
	}
	var p, q *ListNode
	p = dummy
	q = dummy
	for i := 0; i < n; i++ {
		p = p.Next
	}
	for {
		if p.Next == nil {
			break
		}
		p = p.Next
		q = q.Next
	}
	q.Next = q.Next.Next
	return dummy.Next
}
