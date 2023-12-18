#include <iostream>
#include <vector>

using namespace std;

int main() {
    int ySize, xSize;
    cin >> ySize >> xSize;

    vector<vector<int>> board(ySize, vector<int>(xSize, 0));

    while (true) {
        int y, x, val;
        cin >> y >> x >> val;
        y--;
        x--;

        if (y == -1 && x == -1 && val == 0) {
            break;
        } else {
            board[y][x] += val;
        }
    }

    vector<vector<int>> PSAWhite(ySize + 1, vector<int>(xSize + 1, 0));
    vector<vector<int>> PSABlack(ySize + 1, vector<int>(xSize + 1, 0));

    for (int i = 0; i < ySize; ++i) {
        bool isWhite = i % 2 == 0;
        for (int j = 0; j < xSize; ++j) {
            if (isWhite) {
                PSAWhite[i + 1][j + 1] = PSAWhite[i + 1][j] + PSAWhite[i][j + 1] - PSAWhite[i][j] + board[i][j];
                PSABlack[i + 1][j + 1] = PSABlack[i + 1][j] + PSABlack[i][j + 1] - PSABlack[i][j] + 0;
            } else {
                PSABlack[i + 1][j + 1] = PSABlack[i + 1][j] + PSABlack[i][j + 1] - PSABlack[i][j] + board[i][j];
                PSAWhite[i + 1][j + 1] = PSAWhite[i + 1][j] + PSAWhite[i][j + 1] - PSAWhite[i][j] + 0;
            }
            isWhite = !isWhite;
        }
    }

    while (true) {
        int y1, x1, y2, x2;
        cin >> y1 >> x1 >> y2 >> x2;
        y1--;
        x1--;
        y2--;
        x2--;

        if (y1 == -1 && x1 == -1 && y2 == -1 && x2 == -1) {
            break;
        } else {
            int whiteSum = PSAWhite[y2 + 1][x2 + 1] - PSAWhite[y2 + 1][x1] - PSAWhite[y1][x2 + 1] + PSAWhite[y1][x1];
            int blackSum = PSABlack[y2 + 1][x2 + 1] - PSABlack[y2 + 1][x1] - PSABlack[y1][x2 + 1] + PSABlack[y1][x1];

            if (y1 % 2 == 0) {
                if (x1 % 2 == 0) {
                    cout << whiteSum - blackSum << endl;
                } else {
                    cout << blackSum - whiteSum << endl;
                }
            } else {
                if (x1 % 2 == 0) {
                    cout << blackSum - whiteSum << endl;
                } else {
                    cout << whiteSum - blackSum << endl;
                }
            }
        }
    }

    return 0;
}
