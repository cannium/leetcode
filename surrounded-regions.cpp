#include<iostream>
#include<queue>
#include<vector>
#include<string>
using namespace std;

struct position
{
    int x, y;
};

class Solution {
public:
    vector<vector<char> > visited;
    void solve(vector<vector<char> > &board) {
        visited.resize(board.size());
        for(int i = 0; i < board.size(); i++)
        {
            visited[i].resize(board[0].size());
        }

        for(int i = 0; i < board.size(); i++)
        {
            for(int j = 0; j < board[0].size(); j++)
            {
                //cout << i << " " << j << endl;
                if(visited[i][j])
                    continue;
                if(board[i][j] == 'X')
                    continue;

                queue<position> q;
                position temp = {i,j};
                q.push(temp);

                position p;
                const int delta[4][2] = { {0,1}, {1,0}, {0,-1}, {-1,0} };        
                bool needFill = true;
                while(!q.empty())
                {
                    p = q.front();
                    q.pop();

                    if(visited[p.x][p.y])
                        continue;

                    visited[p.x][p.y] = 1;

                    //cout << p.x << " " << p.y << endl;
                    if(p.x == 0 or p.x == board.size() - 1 or \
                                p.y == 0 or p.y == board[0].size() - 1)
                    {
                        needFill = false;
                    }
                    for(int a = 0; a < 4; a++)
                    {
                        position temp = {p.x + delta[a][0], p.y + delta[a][1]};
                        if(temp.x < 0 or temp.x > board.size()-1 or \
                                temp.y < 0 or temp.y > board[0].size()-1)
                        {continue;}
                        if(visited[temp.x][temp.y])
                        {continue;}
                        if(board[temp.x][temp.y] == 'X')
                        {continue;}
                        q.push(temp);
                    }
                }
                //cout << "needFill " << needFill << endl;
                if(needFill)
                    fill(board, i, j);
            }
        }
    }
    void fill(vector<vector<char> > &board, int x, int y)
    {
        queue<position> q;
        position temp = {x,y};
        q.push(temp);
        const int delta[4][2] = { {0,1}, {1,0}, {0,-1}, {-1,0} };        
        while(!q.empty())
        {
            position p = q.front();
            q.pop();
            //cout << "fill " << p.x << " " << p.y << endl;
            if(board[p.x][p.y] == 'X')
                continue;
            board[p.x][p.y] = 'X';
            for(int i = 0; i < 4; i++)
            {
                position temp = {p.x + delta[i][0], p.y + delta[i][1]};
                if(temp.x < 0 or temp.x > board.size()-1 or \
                    temp.y < 0 or temp.y > board[0].size()-1)
                    {continue;}
                if(board[temp.x][temp.y] == 'X')
                    {continue;}
                q.push(temp);
            }
        }
    }
};

void print(vector<vector<char> > & board)
{
    int X = board.size();
    for(int i = 0; i < X; i++)
    {
        for(int j = 0; j < X; j++)
        {
            cout << board[i][j];
        }
        cout << endl;
    }
}

int main()
{
    Solution sol;
//    const int X = 20;
//    char b[X][X+1] = {"OOOOOOOOXOOOOOXOOOOO","OOOOOOOXOOOOOOOOOOOO","XOOXOXOOOOXOOXOOOOOO","OOOOOOOOOOOOOOOOOXXO","OXXOOOOOOXOOOOOOOOOO","OOOOXOOOOOOXOOOOOXXO","OOOOOOOXOOOOOOOOOOOO","OOOOOOOOOOOOOXOOOOOO","OOOOOOOOOOOOOOOOOOXO","OOOOOXOOOOOOOOOOOOOO","OOOOOOOOXOOOOOOOOOOO","OOOOXOOOOXOOOOOOOOOO","OOOOOOOOXOOOOOOOOOOO","XOOOOOOOOXXOOOOOOOOO","OOOOOOOOOOOXOOOOOOOO","OOOOXOOOOOOOOXOOOOOX","OOOOOXOOOOOOOOOXOXOO","OXOOOOOOOOOOOOOOOOOO","OOOOOOOOXXOOOXOOXOOX","OOOOOOOOOOOOOOOOOOOO"};

//    const int X = 3;
//    char b[X][X+1] = {"XXX", "XOX", "XOX"};


    const int X = 4;
    char b[X][X+1] = {"OXXX", "OXOX", "OXOX", "XXXX"};

    vector<vector<char> > board;
    board.resize(X);
    for(int i = 0; i < X; i++)
    {
        board[i].resize(X);
        for(int j = 0; j < X; j++)
        {
            board[i][j] = b[i][j];
        }
    }
    print(board);
    sol.solve(board);
    cout << endl;
    print(board);
}
