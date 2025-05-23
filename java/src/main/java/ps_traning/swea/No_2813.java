package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class No_2813 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.valueOf(st.nextToken());
            int m = Integer.valueOf(st.nextToken());

            List<Integer>[] edges = new List[n + 1];
            for (int i = 1; i <= n; i++) {
                edges[i] = new ArrayList<>();
            }

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.valueOf(st.nextToken());
                int y = Integer.valueOf(st.nextToken());
                edges[x].add(y);
                edges[y].add(x);
            }
            boolean[] visited = new boolean[n + 1];
            int[] temp = recursion(edges, visited, 1, 1);
            int[] result = recursion(edges, visited, temp[1], 1);
            sb.append("#").append(tc).append(" ").append(result[0]).append("\n");
        }
        System.out.print(sb);
    }

    private static int[] recursion(List<Integer>[] edges, boolean[] visited, int node, int depth) {
        int[] result = {depth, node};
        visited[node] = true;
        for (int next : edges[node]) {
            if (visited[next]) continue;
            visited[next] = true;
            int[] temp = recursion(edges, visited, next, depth + 1);
            if (result[0] < temp[0]) result = temp;
            visited[next] = false;
        }
        visited[node] = false;
        return result;
    }
}
