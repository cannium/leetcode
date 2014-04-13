#include<iostream>
#include<string>
#include<vector>

using namespace std;

class Solution {
public:
    vector<vector<int> > isPalindrome;
    vector<vector<string> > partition(string s) {
        isPalindrome.resize(s.size());
        for(int i = 0; i < s.size(); i++)
            isPalindrome[i].resize(s.size());

        return doPartition(s, 0, s.size()-1);
    }
    int minCut(string s) {
    // Time Limit Exceeded...
        isPalindrome.resize(s.size());
        for(int i = 0; i < s.size(); i++)
            isPalindrome[i].resize(s.size());
        
        vector<vector<string> > ans = doPartition(s, 0, s.size()-1);
        vector<vector<string> >::iterator it;
        int minParts = s.size();
        for(it = ans.begin(); it != ans.end(); it++)
        {
            if(minParts > (*it).size())
                minParts = (*it).size();
        }
        return minParts - 1;
    }
    vector<vector<string> > doPartition(string s, int begin, int end)
    // begin and end are inclusive, aka "[begin, end]"
    {
        vector<vector<string> > ans;
        for(int i = begin; i <= end; i++)
        {
            if(decideIfPalindrome(s, begin, i))
            {
                int next = i + 1;
                if(next == end)
                {
                    vector<string> a;
                    a.push_back(s.substr(begin, i-begin+1));
                    a.push_back(s.substr(end, 1));
                    ans.push_back(a);
                }
                else if(next > end)
                {
                    vector<string> a;
                    a.push_back(s.substr(begin, i-begin+1));
                    ans.push_back(a);
                }
                else
                {
                    vector<vector<string> > ret = doPartition(s, next, end);
                    vector<vector<string> >::iterator v;
                    for(v = ret.begin(); v != ret.end(); v++)
                    {
                        (*v).insert((*v).begin(), s.substr(begin, i-begin+1));
                        ans.push_back(*v);
                    }
                }
            }
        }
        return ans;
    }

    bool decideIfPalindrome(string s, int begin, int end)
    {
        if(begin == end)
            return true;
        if(isPalindrome[begin][end] != 0)
        {
            return isPalindrome[begin][end] == 1 ? true:false;
        }
        if(begin + 1 == end or end + 1 == begin)
        {
            if(s[begin] == s[end])
            {
                isPalindrome[begin][end] = 1;
                return true;
            }
            else
            {
                isPalindrome[begin][end] = -1;
                return false;
            }
        }
        if(s[begin] == s[end])
        {
            if(decideIfPalindrome(s, begin+1, end-1))
            {
                isPalindrome[begin][end] = 1;
                return true;
            }
            else
            {
                isPalindrome[begin][end] = -1;
                return false;
            }
        }
        isPalindrome[begin][end] = -1;
        return false;
    }
};


int main()
{
    Solution sol;
    vector<vector<string> > ans = sol.partition("aab");
    vector<vector<string> >::iterator v;
    vector<string>::iterator s;
    for(v = ans.begin(); v != ans.end(); v++)
    {
        for(s = v -> begin(); s != v -> end(); s++)
        {
            cout << *s << " ";
        }
        cout << endl;
    }
    cout << sol.minCut("aab") << endl;
}
