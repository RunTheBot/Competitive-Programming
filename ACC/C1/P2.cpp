#include <vector>
#include <queue>
#include <unordered_map>
#include <iostream>
#include <utility>
using namespace std;

// Union-Find (Disjoint Set Union) Implementation
class UnionFind {
private:
    vector<int> parent, rank;
    
public:
    UnionFind(int n) {
        parent.resize(n);
        rank.resize(n, 1);
        for(int i = 0; i < n; i++) parent[i] = i;
    }
    
    int find(int x) {
        if(parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }
    
    void union_sets(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if(rootX != rootY) {
            if(rank[rootX] > rank[rootY]) {
                parent[rootY] = rootX;
            } else if(rank[rootX] < rank[rootY]) {
                parent[rootX] = rootY;
            } else {
                parent[rootY] = rootX;
                rank[rootX]++;
            }
        }
    }
};

int bidirectional_bfs(vector<vector<int>>& graph, int start, int end) {
    if(start == end) return 0;
    
    queue<pair<int,int>> queue_start, queue_end;
    unordered_map<int,int> visited_start, visited_end;
    
    queue_start.push(make_pair(start, 0));
    queue_end.push(make_pair(end, 0));
    visited_start[start] = 0;
    visited_end[end] = 0;
    
    while(!queue_start.empty() && !queue_end.empty()) {
        pair<int, int> front_pair = queue_start.front();
        int node = front_pair.first;
        int dist = front_pair.second;
        queue_start.pop();
        
        for(int neighbor : graph[node]) {
            if(!visited_start.count(neighbor)) {
                queue_start.push(make_pair(neighbor, dist + 1));
                visited_start[neighbor] = dist + 1;
                if(visited_end.count(neighbor)) {
                    return dist + 1 + visited_end[neighbor];
                }
            }
        }
        
        front_pair = queue_end.front();
        node = front_pair.first;
        dist = front_pair.second;
        queue_end.pop();
        for(int neighbor : graph[node]) {
            if(!visited_end.count(neighbor)) {
                visited_end[neighbor] = dist + 1;
                queue_end.push({neighbor, dist + 1});
                if(visited_start.count(neighbor)) {
                    return dist + 1 + visited_start[neighbor];
                }
            }
        }
    }
    
    return -1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N, M, Q;
    cin >> N >> M >> Q;
    
    vector<vector<int>> graph(N + 1);
    UnionFind uf(N);
    
    for(int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
        uf.union_sets(u - 1, v - 1);
    }
    
    for(int i = 0; i < Q; i++) {
        int a, b;
        cin >> a >> b;
        if(uf.find(a - 1) != uf.find(b - 1)) {
            cout << -1 << "\n";
        } else {
            cout << bidirectional_bfs(graph, a, b) << "\n";
        }
    }
    
    return 0;
}