/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    map<RandomListNode *, RandomListNode *> oldToNew;

    RandomListNode *copyRandomList(RandomListNode *head) {
        if(head == NULL)
            return NULL;

        RandomListNode *newHead = new RandomListNode(head -> label);
        oldToNew[head] = newHead;
        RandomListNode *p = head;
        RandomListNode *q = newHead;
        oldToNew[NULL] = NULL;
        while(p -> next)
        {
            p = p -> next;
            q -> next = new RandomListNode(p -> label);
            oldToNew[p] = q -> next;
            q = q -> next;
        }
        p = head;
        q = newHead;
        while(p)
        {
            q -> random = oldToNew[p -> random];
            p = p -> next;
            q = q -> next;
        }
        return newHead;
    }
};
