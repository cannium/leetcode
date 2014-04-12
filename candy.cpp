#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    int length;
    vector<int> candyForChild;
    vector<int> ratings;
    int candy(vector<int> &ratings) {
        this -> ratings = ratings;
        length = ratings.size();
        for(int i = 0; i < length; i++)
        {
            candyForChild.push_back(0);
        }
        int sum = 0;
        for(int i = 0; i < length; i++)
        {
            sum += getCandy(i);
        }
        return sum;
    }
    int getCandy(int i)
    {
        if(candyForChild[i])
            return candyForChild[i];

        int a = 1;
        int b = 1;
        if(i != 0)
        {
            if(ratings[i-1] < ratings[i])
            {
                a = getCandy(i-1) + 1;
            }
        }
        if(i != length - 1)
        {
            if(ratings[i+1] < ratings[i])
            {
                b = getCandy(i+1) + 1;
            }
        }
        candyForChild[i] = a > b ? a : b;
        return candyForChild[i];
    }
};

int main()
{
    Solution s;
    int v[] = {1,2,3,4,1,2,1,2,3};
    vector<int> r(begin(v), end(v));
    cout << s.candy(r) << endl;
}
