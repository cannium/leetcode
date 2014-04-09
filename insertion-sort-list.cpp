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
    ListNode *insertionSortList(ListNode *head) {
        ListNode *sorted = NULL;
        while(head != NULL)
        {
            if(sorted == NULL)
            {
                sorted = head;
                head = head -> next;
                sorted -> next = NULL;
                continue;
            }
            if(head -> val < sorted -> val)
            {
                ListNode *temp = sorted;
                sorted = head;
                head = head -> next;
                sorted -> next = temp;
                continue;
            }
            ListNode *p = sorted;
            for( ; p != NULL and p -> next != NULL; p = p -> next)
            {
                if(head -> val < p -> next -> val)
                    break;
            }
            ListNode *temp = p -> next;
            p -> next = head;
            head = head -> next;
            p -> next -> next = temp;
        }
        return sorted;
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
