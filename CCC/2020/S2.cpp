#include <iostream>
#include <vector>
#include <queue>
#include <cmath>
using namespace std;

const int MAX_M = 1000;
const int MAX_N = 1000;
const int MAX_VAL = 1000001;

int maze[MAX_M][MAX_N];
bool visited[MAX_M + 1][MAX_N + 1];
bool duplicate[MAX_VAL + 1];

bool isInside(pair<int, int> mazeSize, pair<int, int> pose) {
    return 0 <= pose.first && pose.first < mazeSize.first &&
           0 <= pose.second && pose.second < mazeSize.second;
}

vector<int> findFactors(int num) {
    vector<int> factors;
    for (int i = 1; i <= sqrt(num); ++i) {
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

bool BFS(pair<int, int> start, pair<int, int> end, pair<int, int> mazeSize) {
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

int main() {
    int M, N;
    cin >> M >> N;
    pair<int, int> mazeSize = make_pair(M, N);

    for (int i = 0; i < M; ++i) {
        for (int j = 0; j < N; ++j) {
            cin >> maze[i][j];
        }
    }

    pair<int, int> start = make_pair(0, 0);
    pair<int, int> end = make_pair(M - 1, N - 1);

    if (BFS(start, end, mazeSize)) {
        cout << "yes" << endl;
    } else {
        cout << "no" << endl;
    }

    return 0;
}
