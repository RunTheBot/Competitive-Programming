#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

void build(vector<long long>& a, int n, vector<long long>& segtree) {
    for (int i = 0; i < n; i++) {
        segtree[n + i] = a[i];
    }
    for (int i = n - 1; i > 0; i--) {
        segtree[i] = segtree[2 * i] + segtree[2 * i + 1];
    }
}

void update(int index, long long val, int n, vector<long long>& segtree) {
    index += n;
    segtree[index] = val;
    while (index > 1) {
        index /= 2;
        segtree[index] = segtree[2 * index] + segtree[2 * index + 1];
    }
}

long long query_tree(int left, int right, int n, vector<long long>& segtree) {
    left += n;
    right += n;
    long long sum = 0;
    while (left < right) {
        if (left & 1) {
            sum += segtree[left];
            left += 1;
        }
        if (right & 1) {
            right -= 1;
            sum += segtree[right];
        }
        left  /= 2;
        right /= 2;
    }
    return sum;
}

vector<string> split(const string& s) {
    vector<string> tokens;
    stringstream ss(s);
    string token;
    while (getline(ss, token, ' ')) {
        tokens.push_back(token);
    }
    return tokens;
}

int main() {
    int n, q;
    cin >> n >> q;

    vector<long long> inputArr(n);
    for (int i = 0; i < n; i++) {
        cin >> inputArr[i];
    }

    vector<long long> tree(2 * n);

    build(inputArr, n, tree);

    cin.ignore();
    for (int _ = 0; _ < q; _++) {
        string line;
        getline(cin, line);
        vector<string> query = split(line);
        if (query[0] == "S") {
            int l = stoi(query[1]);
            int r = stoi(query[2]);
            cout << query_tree(l - 1, r, n, tree) << endl;
        } else {
            int i = stoi(query[1]);
            long long x = stoll(query[2]);
            update(i - 1, x, n, tree);
        }
    }

    return 0;
}
