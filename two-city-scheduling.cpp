    bool cmpf(pair<int, int> a, pair<int, int> b) {
        return a.first < b.first;
    }

class Solution {

public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        vector<pair<int, int>> ab(costs.size());
        vector<int> visitab(costs.size(), 0);
        for (int i = 0; i < costs.size(); i++) {
            ab[i] = make_pair(costs[i][0] - costs[i][1], i);
        }
        sort(ab.begin(), ab.end(), cmpf);
        int ans = 0;
        for (int i = 0; i < costs.size()/2; i++) {
            int ii = ab[i].second;
            ans += costs[ii][0];
            visitab[ii] = 1;
        }
        for (int i = 0; i < costs.size(); i++) {
            if (visitab[i] != 1) {
                ans += costs[i][1];
            }
        }
        return ans;
    }
};
