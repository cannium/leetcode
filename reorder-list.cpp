#include<iostream>
#include<vector>
using namespace std;
/**
 * Definition for singly-linked list.
 */
  struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
  };

class Solution {
public:
    void reorderList(ListNode *head) {
        if(head == NULL)
            return;
        ListNode *slow = head;
        ListNode *fast = head;
        while(slow and fast and fast -> next and fast -> next -> next)
        {
            slow = slow -> next;
            fast = fast -> next -> next;
        }
        ListNode *a = head;
        ListNode *b = slow -> next;
        slow -> next = NULL;
        b = reverse(b);
        ListNode *ans = a;
        a = a -> next;
        ListNode *p = ans;
        while(a)
        {
            p -> next = b;
            b = b -> next;
            
            p = p -> next;
            p -> next = a;
            a = a -> next;

            p = p -> next;
        }
        if(b)
            p -> next = b;
        head = ans;
        //return head;
    }

    ListNode* reverse(ListNode *head)
    {
        if(head == NULL or head -> next == NULL)
            return head;
        ListNode *p = head;
        ListNode *last = NULL;
        while(1)
        {
            ListNode *next = p -> next;
            p -> next = last;
            last = p;
            if(next == NULL)
                return p;
            else
                p = next;
        }
    }
};


ListNode* buildList(vector<int> l)
{
    ListNode *list = NULL;
    ListNode *p = NULL;
    for(int i = 0; i < l.size(); i++)
    {
        if(list == NULL)
        {
            list = new ListNode(l[i]);
            p = list;
        }
        else
        {
            p -> next = new ListNode(l[i]);
            p = p -> next;
        }
    }
    return list;
}

void printList(ListNode *l)
{
    while(l)
    {
        cout << l -> val << ' ';
        l = l -> next;
    }
    cout << endl;
}

int main()
{
    Solution s;
    int vv[] = {1,2,3,4,5};
    vector<int> v(&vv[0], &vv[0]+5);
    ListNode* res = s.reorderList(buildList(v));
    printList(res);
}
