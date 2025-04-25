package ps_traning.solvedAC.class_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class No_15681 {
    private static int n, r, q;
    private static List<Integer>[] nodes;
    private static boolean[] visited;
    private static int[] nodeCnt;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.valueOf(st.nextToken());
        r = Integer.valueOf(st.nextToken());
        q = Integer.valueOf(st.nextToken());

        nodes = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            nodes[i] = new ArrayList<>();
        }
        visited = new boolean[n + 1];
        nodeCnt = new int[n + 1];

        for (int i = 0; i < n - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.valueOf(st.nextToken());
            int v = Integer.valueOf(st.nextToken());
            nodes[u].add(v);
            nodes[v].add(u);
        }

        visited[r] = true;
        checkTree(r);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < q; i++) {
            sb.append(nodeCnt[Integer.valueOf(br.readLine())]).append("\n");
        }
        System.out.print(sb.toString());
    }

    private static int checkTree(int node) {
        int cnt = 1;
        for (int nextNode : nodes[node]) {
            if (visited[nextNode]) continue;
            visited[nextNode] = true;
            cnt += checkTree(nextNode);
        }
        nodeCnt[node] = cnt;
        return cnt;
    }
}
