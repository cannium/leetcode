#include<map>
#include<vector>
#include<set>
#include<unordered_set>
#include<string>
#include<iostream>
using namespace std;

class Solution {
    map<string, vector<string> > bookkeeping;
public:
    Solution()
    {
        bookkeeping.clear();
    }
    vector<string> wordBreak(string s, unordered_set<string> &dict) {
        if(bookkeeping.count(s) != 0)
            return bookkeeping[s];

        vector<string> ans;

        unordered_set<string>::iterator it;
        for(it = dict.begin(); it != dict.end(); it++)
        {
            if(s.substr(0, (*it).size()) == *it) // startswith
            {
                if(s == *it)
                    ans.push_back(s);
                else
                {
                    vector<string> res;
                    res = wordBreak(s.substr((*it).size(), s.size()), dict);
                    if(res.empty())
                        continue;
                    vector<string>::iterator it2;
                    for(it2 = res.begin(); it2 != res.end(); it2++)
                    {
                        ans.push_back(*it + " " + *it2);
                    }
                }
            }
        }
        bookkeeping[s] = ans;
        return ans;
    }
};

int main()
{
    Solution s;
    string str = "catsanddog";
    string tmp[] = {"cat", "cats", "and", "sand", "dog"};
    unordered_set<string> d(tmp, tmp + sizeof(tmp) / sizeof(tmp[0]));
    vector<string> ans = s.wordBreak(str, d);
    vector<string>::iterator it;
    for(it = ans.begin(); it != ans.end(); it++)
    {
        cout << *it << endl;
    }
}
