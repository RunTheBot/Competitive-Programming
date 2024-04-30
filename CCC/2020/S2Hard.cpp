#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
using namespace std;

const int MAX_M = 4001;
const int MAX_N = 4001;
const int MAX_VAL = MAX_M * MAX_N;

bool visited[MAX_M + 2][MAX_N + 2];
bool duplicate[MAX_VAL + 2];

bool isInside(pair<int, int> mazeSize, pair<int, int> pose) {
    return 0 <= pose.first && pose.first < mazeSize.first &&
           0 <= pose.second && pose.second < mazeSize.second;
}

vector<int> findFactors(int num) {
    vector<int> factors;
    for (int i = 1; i <= (int)(sqrt(num)+0.1); ++i) {
        if (num % i == 0) {
            if (num / i == i) {
                factors.push_back(i);
            } else {
                factors.push_back(i);
                factors.push_back(num / i);
            }
        }
    }
    return factors;
}

bool BFS(pair<int, int> start, pair<int, int> end, pair<int, int> mazeSize, vector<vector<int>>& maze) {
    queue<pair<int, int>> q;
    q.push(start);
    visited[start.first][start.second] = true;
    duplicate[maze[start.first][start.second]] = true;

    while (!q.empty()) {
        pair<int, int> currentPos = q.front();
        q.pop();
        int r = currentPos.first;
        int c = currentPos.second;
        int currentVal = maze[r][c];

        for (int factor : findFactors(currentVal)) {
            pair<int, int> nextPossiblePos = make_pair(factor - 1, (currentVal / factor) - 1);
            if (isInside(mazeSize, nextPossiblePos)) {
                if (nextPossiblePos == end) {
                    return true;
                }
                if (!visited[nextPossiblePos.first][nextPossiblePos.second] && !duplicate[maze[nextPossiblePos.first][nextPossiblePos.second]]) {
                    visited[nextPossiblePos.first][nextPossiblePos.second] = true;
                    q.push(nextPossiblePos);
                    duplicate[maze[nextPossiblePos.first][nextPossiblePos.second]] = true;
                }
            }
        }
    }
    return false;
}

bool can_escape(int M, int N, vector<vector<int>> v) {
    if (M == 1 && N == 1) {
        return true;
    }
    pair<int, int> mazeSize = make_pair(M, N);

    for (int i = 0; i < M + 1; ++i) {
        for (int j = 0; j < N + 1; ++j) {
            visited[i][j] = false;
        }
    }

    for (int i = 0; i < MAX_VAL + 1; ++i) {
        duplicate[i] = false;
    }

    pair<int, int> start = make_pair(0, 0);
    pair<int, int> end = make_pair(M - 1, N - 1);

    return BFS(start, end, mazeSize, v);
}

int main() {
    int M, N;
    cin >> M >> N;
    pair<int, int> mazeSize = make_pair(M, N);

    vector<vector<int>> maze(M, vector<int>(N));

    for (int i = 0; i < M; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> maze[i][j];
        }
    }

    pair<int, int> start = make_pair(0, 0);
    pair<int, int> end = make_pair(M - 1, N - 1);

    if (can_escape(M, N, maze)) {
        cout << "yes" << endl;
    } else {
        cout << "no" << endl;
    }

    return 0;
}