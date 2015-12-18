
//Definition for singly-linked list.
function ListNode(val) {
    this.val = val;
    this.next = null;
}

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    var ans = null, p = null;
    var carry = 0;
    while(l1 || l2 || carry) {
        var digit = carry;
        if(l1) {
            digit += l1.val;
            l1 = l1.next;
        }
        if(l2) {
            digit += l2.val;
            l2 = l2.next;
        }
        carry = 0;
        if(digit >= 10) {
            digit -= 10;
            carry = 1;
        }
        if(p === null) {
            p = new ListNode(digit);
            ans = p;
        } else {
            p.next = new ListNode(digit);
            p = p.next;
        }
    }
    return ans;
};

var createList = function(array) {
    var ans = null, p = null;
    for(var i = 0; i < array.length; i++) {
        if(p === null) {
            p = new ListNode(array[i]);
            ans = p;
        } else {
            p.next = new ListNode(array[i]);
            p = p.next;
        }
    }
    return ans;
}

var printList = function(list) {
    var ans = [];
    while(list) {
        ans.push(list.val);
        list = list.next;
    }
    console.log(ans);
}
