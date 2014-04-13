#include<iostream>
#include<string>
#include<vector>

using namespace std;

class Solution {
public:
    vector<vector<char> > isPalindrome;
    vector<int> cuts;
    int minCut(string s)
    {
        isPalindrome.resize(s.size());
        cuts.resize(s.size());
        cuts[0] = 1; // offset by 1
        for(int i = 0; i < s.size(); i++)
        {
            isPalindrome[i].resize(s.size());
        }
        
        makePalindromeTable(s);
        return doCalc(s, s.size()-1);
    }

    void makePalindromeTable(string s)
    {
        int n = s.size();
        // The calculation order is:
        // (0,0) (1,1) (2,2) ... ... (n-1,n-1)
        // (0,1) (1,2) (2,3) .. (n-2,n-1)
        // ...
        // (0, n-2) (1, n-1)
        // (0, n-1)
        // Learn from http://oj.leetcode.com/discuss/496/always-time-limit-exceeded
        // really smart.
        for(int len = 1; len <= n; len++)
        {
            for(int i = 0; i <= n - len; i++)
            {
                int j = i + len - 1;
                if(i == j) isPalindrome[i][j] = 1;
                else if(j == i + 1 and s[i] == s[j]) isPalindrome[i][j] = 1;
                else if(isPalindrome[i+1][j-1] and s[i] == s[j])
                    isPalindrome[i][j] = 1;
            }
        }
    }

    int doCalc(string s, int end)
    {
        if(cuts[end])
            return cuts[end] - 1; // offset by 1 so we could use "0" as
                                  //  "not calculated yet"
        if(isPalindrome[0][end])
        {
            cuts[end] = 1;  // offset by 1
            return 0;
        }

        int min = end + 1;
        for(int i = 0; i < end; i++)
        {
            if(isPalindrome[i+1][end])
            {
                min = min > doCalc(s, i) + 1 ? doCalc(s, i) + 1 : min;
            }
        }
        cuts[end] = min + 1; // offset by 1
        return min;
    }

    bool decideIfPalindrome(string s, int begin, int end)
    // Memory Limit Exceeded...
    //
    // begin and end are inclusive, aka "[begin, end]"
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
    cout << sol.minCut("aab") << endl;
    //cout << sol.minCut("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") << endl;
}
