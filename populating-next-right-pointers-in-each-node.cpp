#include<iostream>
#include<vector>
using namespace std;

// Definition for binary tree with next pointer.
 struct TreeLinkNode {
  int val;
  TreeLinkNode *left, *right, *next;
  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 };

class Solution {
public:
    void connect(TreeLinkNode *root) {
        if(root == NULL)
            return;

        vector<TreeLinkNode *> q[2];
        int qNum = 0;
        q[0].push_back(root);
        while(!q[qNum].empty())
        {
            int n = q[qNum].size();
            for(int i = 0; i < n; i++)
            {
                if(q[qNum][i]->left)
                { q[1-qNum].push_back(q[qNum][i]->left);}
                if(q[qNum][i]->right)
                { q[1-qNum].push_back(q[qNum][i]->right);}

                if(i == n - 1)
                { q[qNum][i]->next = NULL;}
                else
                { q[qNum][i]->next = q[qNum][i+1];}
            }
            q[qNum].clear();
            qNum = 1 - qNum;
        }
    }
};
