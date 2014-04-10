/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        ListNode *slow = head;
        ListNode *fast = head;
        while(slow and fast)
        {
            fast = fast -> next;
            if(fast)
                fast = fast -> next;
            slow = slow -> next;
            if(slow == NULL or fast == NULL)
                return NULL;
            if(slow == fast)
                break;
        }
        slow = head;
        while(slow != fast)
        {
            slow = slow -> next;
            fast = fast -> next;
        }
        return slow;
    }
};
