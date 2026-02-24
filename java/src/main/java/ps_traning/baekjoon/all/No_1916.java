package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class No_1916 {

    private static int n, m;
    private static List<int[]>[] edges;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        edges = new List[n + 1];
        for (int i = 0; i <= n; i++) edges[i] = new ArrayList();

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            edges[s].add(new int[]{e, cost});
        }

        boolean[] visited = new boolean[n + 1];

        StringTokenizer st = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            return a[1] - b[1];
        });

        int answer = 0;
        pq.offer(new int[]{s, 0});
        while (!pq.isEmpty()) {
            int[] poll = pq.poll();
            int node = poll[0], cost = poll[1];
            if (visited[node]) continue;
            visited[node] = true;
            if (node == e) {
                answer = cost;
                break;
            }
            for (int[] info : edges[node]) {
                int next = info[0], plus = info[1];
                if (visited[next]) continue;
                pq.offer(new int[]{next, cost + plus});
            }
        }

        System.out.println(answer);
    }
}
