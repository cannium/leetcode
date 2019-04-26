class Solution {
public:
    vector<vector<int>> allCellsDistOrder(int R, int C, int r0, int c0) {
        vector<vector<int>> cells;
        cells.reserve(R*C);
        for(int r = 0; r < R; r++) {
            for(int c = 0; c < C; c++) {
                cells.push_back(vector<int>{r, c});
            }
        }
        sort(cells.begin(), cells.end(), [r0, c0](vector<int> a, vector<int> b) -> bool {
    int la = abs(r0 - a[0]) + abs(c0 - a[1]);
    int lb = abs(r0 - b[0]) + abs(c0 - b[1]);
    return la < lb;
});
        return cells;
    }
};
