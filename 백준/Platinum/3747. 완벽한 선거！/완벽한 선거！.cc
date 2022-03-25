#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <stack>
using namespace std;
struct TwoSAT {
    int n, c, sccc;
    vector<vector<int>> vt;
    vector<int> disc, scc;
    TwoSAT(int n) :n(n) {
        disc.assign(2 * n + 1, 0);
        scc.assign(2 * n + 1, 0);
        vt.resize(2 * n + 1);
        c = 0;
    }
    stack<int> st;
    int dfs(int here) {
        st.push(here);
        disc[here] = ++c;
        int ret = disc[here];
        for (int i = 0; i < vt[here].size(); i++) {
            int there = vt[here][i];
            if (!disc[there])
                ret = min(ret, dfs(there));
            else if (!scc[there])
                ret = min(ret, disc[there]);
        }
        if (ret == disc[here]) {
            sccc++;
            while (st.size()) {
                int h = st.top();
                st.pop();
                scc[h] = sccc;
                if (h == here)break;
            }
        }
        return ret;
    }
    int cvt(int x) {
        if (x <= n)
            return x + n;
        else
            return x - n;
    }
    void addEdge(int x, int y) {
        vt[cvt(x)].push_back(y);
        vt[cvt(y)].push_back(x);
    }
    bool isSatisfied(){
        for (int i = 1; i <= 2 * n; i++)
            if (!disc[i])dfs(i);
        for (int i = 1; i <= n; i++)
            if (scc[i] == scc[cvt(i)])
                return false;
        return true;
    }
};
int n, m, x, y;
int main() {
    while (scanf("%d%d", &n, &m) != EOF) {
        TwoSAT tsat(n);
        for (int i = 0; i < m; i++) {
            scanf("%d%d", &x, &y);
            if (x < 0)x = tsat.cvt(-x);
            if (y < 0)y = tsat.cvt(-y);
            tsat.addEdge(x, y);
        }
        printf("%d\n", tsat.isSatisfied() ? 1 : 0);
    }
    return 0;
}