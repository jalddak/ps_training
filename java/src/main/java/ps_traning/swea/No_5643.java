package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class No_5643 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            int n = Integer.valueOf(br.readLine());
            int m = Integer.valueOf(br.readLine());
            List<Integer>[] tallEdges = new List[n];
            List<Integer>[] smallEdges = new List[n];
            for (int i = 0; i < n; i++) {
                tallEdges[i] = new ArrayList<>();
                smallEdges[i] = new ArrayList<>();
            }
            for (int i = 0; i < m; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int s = Integer.valueOf(st.nextToken()) - 1;
                int e = Integer.valueOf(st.nextToken()) - 1;
                tallEdges[s].add(e);
                smallEdges[e].add(s);
            }
            int result = 0;

            for (int i = 0; i < n; i++) {
                int cnt = 0;
                boolean[] visited = new boolean[n];
                visited[i] = true;
                cnt += dfs(tallEdges, visited, i);
                visited = new boolean[n];
                visited[i] = true;
                cnt += dfs(smallEdges, visited, i);
                if (cnt == n - 1) result++;
            }

            sb.append("#").append(tc).append(" ").append(result).append("\n");
        }
        System.out.print(sb);
    }

    private static int dfs(List<Integer>[] edges, boolean[] visited, int node) {
        int result = 0;
        for (int next : edges[node]) {
            if (visited[next]) continue;
            visited[next] = true;
            result += 1;
            result += dfs(edges, visited, next);
        }
        return result;
    }
}
