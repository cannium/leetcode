class Solution {
private:
    vector<int> how(vector<int>& A, int l) {
        vector<int> ans(A.size(), 0);
        int cur = 0;
        for (int i = 0; i < l; i++) {
            cur += A[i];
        }
        ans[0] = cur;
        for (int i = l; i < A.size(); i++) {
            cur = cur + A[i] - A[i-l];
            ans[i-l+1] = cur;
        }
        return ans;
    }
    vector<int> backward_max(vector<int>& a) {
        vector<int> ans(a.size(), 0);
        int cur = 0;
        for (int i = a.size()-1; i >= 0; i--) {
            cur = max(a[i], cur);
            ans[i] = cur;
        }
        return ans;
    }
    int combine(vector<int>& l, int L, vector<int>& mmax) {
        int ans = 0;
        for(int i = 0; i < l.size(); i++) {
            if (i+L >= l.size()) {
                ans = max(ans, l[i]);
            } else {
                ans = max(ans, l[i] + mmax[i+L]);
            }
        }
        return ans;
    }
    void print(vector<int>& A) {
        for(int i = 0; i < A.size(); i++) {
            cout << A[i] << "  ";
        }
        cout << endl;
    }
public:
    int maxSumTwoNoOverlap(vector<int>& A, int L, int M) {
        auto l = how(A, L);
        auto m = how(A, M);
        //print(l);
        //print(m);
        auto lmax = backward_max(l);
        auto mmax = backward_max(m);
        //print(lmax);
        //print(mmax);
        int a1 = combine(l, L, mmax);
        int a2 = combine(m, M, lmax);
        return max(a1, a2);
    }
};
