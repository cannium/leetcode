#include<iostream>
#include<unordered_set>
#include<set>
#include<string>
#include<map>
#include<queue>
#include<stack>

using namespace std;

class Solution {
public:
    map<string, vector<string> > wordToLast;
    vector<vector<string> > findLadders(string start, string end, unordered_set<string> &dict) {
        vector<vector<string> > ans;
        queue<string> q[2];
        q[0].push(start);
        dict.erase(start);
        int qNum = 0;
        while(1)
        {
            bool found = false;
            set<string> visited;
            while(!q[qNum].empty())
            {
                string p = q[qNum].front();
                q[qNum].pop();
                
                //cout << p << endl;
                for(int i = 0; i < p.size(); i++)
                {
                    for(char j = 'a'; j <= 'z'; j++)
                    {
                        if(p[i] == j)
                            continue;

                        string original = p;
                        p[i] = j;
                        if(p == end)
                        {
                            found = true;
                            wordToLast[end].push_back(original);
                        }
                        else if(dict.count(p) > 0)
                        {
                            cout << original << " pushed " << p << endl;
                            wordToLast[p].push_back(original);
                            if(find(visited.begin(), visited.end(), p)==visited.end())
                            {
                                // not visited
                                q[1-qNum].push(p);
                                visited.insert(p);
                            }
                        }
                        p = original;
                    }
                }
            }
            if(found)
                break;
            if(q[qNum].empty() and q[1-qNum].empty())
                return ans;
            for(set<string>::iterator it=visited.begin();it!=visited.end();it++)
            {
                dict.erase(*it);
            }
            qNum = 1 - qNum;
        }

        stack<vector<string> > rev;
        vector<string> temp;
        temp.push_back(end);
        rev.push(temp);
        while(!rev.empty())
        {
            vector<string> s = rev.top();
            rev.pop();
            if(s[0] == start)
            {
                ans.push_back(s);
                continue;
            }
            vector<string>::iterator it;
            for(it = wordToLast[s[0]].begin(); it != wordToLast[s[0]].end(); it++)
            {
                vector<string> temp = s;
                temp.insert(temp.begin(), *it);
                rev.push(temp);
            }
        }
        return ans;
    }
    void printMap()
    {
        map<string, vector<string> >::iterator i;
        vector<string>::iterator j;
        for(i = wordToLast.begin(); i != wordToLast.end(); i++)
        {
            cout << i -> first << ": ";
            for(j = (i->second).begin(); j != (i->second).end(); j++)
            {
                cout << (*j) << " ";
            }
            cout << endl;
        }
    }
};

int main()
{
    unordered_set<string> s;
    // hit cog
    //string str[] = {"hot","dot","dog","lot","log"};
    //for(int i = 0; i < 5; i++)

    // red tax
    string str[] = {"ted","tex","red","tax","tad","den","rex","pee"};
    for(int i = 0; i < 8; i++)
    {
        s.insert(str[i]);
    }
    Solution sol;
    vector<vector<string> > ans = sol.findLadders("red", "tax", s);

    for(vector<vector<string> >::iterator i = ans.begin(); i != ans.end(); i++)
    {
        for(vector<string>::iterator j = (*i).begin(); j != (*i).end(); j++)
        {
            cout << (*j) << " ";
        }
        cout << endl;
    }
    sol.printMap();
}
