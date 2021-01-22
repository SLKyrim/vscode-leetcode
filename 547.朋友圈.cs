public class Solution
{
    public int FindCircleNum(int[][] isConnected)
    {
        int n = isConnected.GetLength(0);
        int m = isConnected[0].GetLength(0);

        UnionFind uf = new UnionFind(n);

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                if (j != i && isConnected[i][j] == 1)
                {
                    uf.union(i, j);
                }
            }
        }

        for (int i = 0; i < n; i++)
        {
            uf.find(i);
        }
        for (int i = 0; i < n; i++)
        {
            uf.find(i);
        }
        List<int> pt = new List<int>(uf.p);
        HashSet<int> hs = new HashSet<int>(pt);
        return hs.Count;
    }

    private class UnionFind
    {
        public int[] p;

        public UnionFind(int n)
        {
            this.p = new int[n];
            for (int i = 0; i < n; i++)
            {
                this.p[i] = i;
            }
        }

        public int find(int i)
        {
            while (i != this.p[i])
            {
                this.p[i] = this.p[this.p[i]];
                i = this.p[i];
            }
            return this.p[i];
        }

        public void union(int id1, int id2)
        {
            id1 = find(id1);
            id2 = find(id2);
            this.p[id1] = id2;
        }

        public bool isConn(int id1, int id2)
        {
            return this.find(id1) == this.find(id2);
        }
    }
}