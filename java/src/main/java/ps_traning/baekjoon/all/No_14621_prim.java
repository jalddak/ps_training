package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class No_14621_prim {

    private static int n, m;
    private static char[] g;
    private static boolean[] visited;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        g = new char[n];
        visited = new boolean[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            g[i] = Character.valueOf(st.nextToken().charAt(0));
        }

        int answer = 0;

        List<int[]>[] edges = new List[n];
        for (int i = 0; i < n; i++) {
            edges[i] = new ArrayList();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int f = Integer.parseInt(st.nextToken()) - 1;
            int s = Integer.parseInt(st.nextToken()) - 1;
            int cost = Integer.parseInt(st.nextToken());

            if (g[f] == g[s]) {
                continue;
            }
            edges[f].add(new int[]{s, cost});
            edges[s].add(new int[]{f, cost});
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            return a[1] - b[1];
        });

        pq.offer(new int[]{0, 0});
        int count = 0;
        while (!pq.isEmpty()) {
            int[] poll = pq.poll();
            int node = poll[0], cost = poll[1];
            if (visited[node]) continue;
            visited[node] = true;
            count += 1;
            answer += cost;

            if (count == n) break;

            for (int[] edge : edges[node]) {
                int next = edge[0], nCost = edge[1];
                if (visited[next]) continue;
                pq.offer(new int[]{next, nCost});
            }
        }

        System.out.println(count == n ? answer : -1);
    }
}
