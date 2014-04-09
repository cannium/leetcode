#include<iostream>
#include<vector>

using namespace std;

struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
  };

class Solution {
public:
    ListNode *sortList(ListNode *head)
    {
        if(head == NULL or head -> next == NULL)
            return head;
        ListNode *slow = head;
        ListNode *fast = head;
        while(slow and fast)
        {
            if(fast -> next == NULL)
                break;
            fast = fast -> next;
            if(fast == NULL or fast -> next == NULL)
                break;
            slow = slow -> next;
            fast = fast -> next;
        }
        ListNode *a = head;
        ListNode *b = slow -> next;
        slow -> next = NULL;
        a = sortList(a);
        b = sortList(b);

        ListNode *newList = NULL;
        ListNode *p = NULL;
        while(a and b)
        {
            if(a -> val <= b -> val)
            {
                if(newList == NULL)
                {
                    newList = a;
                    a = a -> next;
                    newList -> next = NULL;
                    p = newList;
                }
                else
                {
                    p -> next = a;
                    a = a -> next;
                    p = p -> next;
                    p -> next = NULL;
                }
            }
            else
            {
                if(newList == NULL)
                {
                    newList = b;
                    b = b -> next;
                    newList -> next = NULL;
                    p = newList;
                }
                else
                {
                    p -> next = b;
                    b = b -> next;
                    p = p -> next;
                    p -> next = NULL;
                }
            }
        }
        if(a)
        {
            p -> next = a;
        }
        else
        {
            p -> next = b;
        }
        return newList;
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
    int vv[] = {3,2,5,1,7};
    vector<int> v(&vv[0], &vv[0]+5);
    ListNode* res = s.insertionSortList(buildList(v));
    //ListNode* res = s.insertionSortList(NULL);
    printList(res);
}
