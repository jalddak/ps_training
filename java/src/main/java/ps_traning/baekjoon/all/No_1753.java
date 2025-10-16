package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class No_1753 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());

        int start = Integer.parseInt(br.readLine());

        List<int[]>[] edges = new List[n + 1];
        for (int i = 1; i <= n; i++) edges[i] = new ArrayList<>();
        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            edges[u].add(new int[]{w, v});
        }

        int INF = n * 10 + 1;
        int[] result = new int[n + 1];
        Arrays.fill(result, INF);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            if (a[0] == b[0]) return a[1] - b[1];
            return a[0] - b[0];
        });

        pq.offer(new int[]{0, start});
        while (!pq.isEmpty()) {
            int[] poll = pq.poll();
            int cost = poll[0], cur = poll[1];
            if (result[cur] <= cost) continue;
            result[cur] = cost;

            for (int[] info : edges[cur]) {
                int w = info[0], node = info[1];
                if (result[node] <= cost + w) continue;
                pq.offer(new int[]{cost + w, node});
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            int r = result[i];
            sb.append(r == INF ? "INF" : r).append("\n");
        }
        System.out.println(sb);
    }
}
