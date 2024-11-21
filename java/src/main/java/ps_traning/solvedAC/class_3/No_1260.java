package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_1260 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken());
        int m = Integer.valueOf(st.nextToken());
        int v = Integer.valueOf(st.nextToken());

        List<Integer>[] edges = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            edges[i] = new ArrayList<>();
        }
        boolean[] visited = new boolean[n + 1];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.valueOf(st.nextToken());
            int e = Integer.valueOf(st.nextToken());
            edges[s].add(e);
            edges[e].add(s);
        }

        for (int i = 0; i <= n; i++) {
            Collections.sort(edges[i]);
        }

        StringBuilder sb = new StringBuilder();
        List<Integer> result = new ArrayList<>();
        dfs(v, edges, visited, result);
        for (int r : result) sb.append(r).append(" ");
        sb.append("\n");

        result.clear();
        Arrays.fill(visited, false);
        bfs(v, edges, visited, result);
        for (int r : result) sb.append(r).append(" ");

        System.out.println(sb.toString());

    }

    public static void dfs(int v, List<Integer>[] edges, boolean[] visited, List<Integer> result) {
        visited[v] = true;
        result.add(v);
        for (int n : edges[v]) {
            if (!visited[n]) dfs(n, edges, visited, result);
        }
    }

    public static void bfs(int v, List<Integer>[] edges, boolean[] visited, List<Integer> result) {
        Queue<Integer> queue = new LinkedList<>(List.of(v));
        visited[v] = true;
        while (!queue.isEmpty()) {
            v = queue.poll();
            result.add(v);
            for (int n : edges[v]) {
                if (!visited[n]) {
                    visited[n] = true;
                    queue.add(n);
                }
            }
        }
    }
}
