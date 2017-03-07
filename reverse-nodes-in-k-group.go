package main

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

func reverse(head *ListNode) (newHead *ListNode, newTail *ListNode) {
	p := head
	q := head.Next
	for {
		tmp := q.Next
		q.Next = p
		p = q
		q = tmp
		if q == nil {
			break
		}
	}
	return p, head
}

func reverseKGroup(head *ListNode, k int) *ListNode {
	if k == 1 {
		return head
	}
	if head == nil {
		return nil
	}
	groupHead := head
	lastHead := head
	p := head
	for {
		h := p
		for i := 1; i < k; i++ {
			if p.Next != nil {
				p = p.Next
			} else {
				return groupHead
			}
		}
		next := p.Next
		p.Next = nil
		newHead, newTail := reverse(h)
		if groupHead == head {
			groupHead = newHead
		} else {
			lastHead.Next = newHead
			lastHead = newTail
		}
		newTail.Next = next
		p = next
		if next == nil {
			break
		}
	}
	return groupHead
}
