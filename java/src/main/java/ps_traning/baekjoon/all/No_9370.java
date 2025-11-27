package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class No_9370 {

    private static int n, m, t, s, g, h;
    private static List<int[]>[] edges;
    private static Set<Integer> set;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int tcCnt = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        for (int tc = 0; tc < tcCnt; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            m = Integer.parseInt(st.nextToken());
            t = Integer.parseInt(st.nextToken());

            edges = new List[n + 1];
            for (int i = 1; i <= n; i++) {
                edges[i] = new ArrayList<>();
            }

            st = new StringTokenizer(br.readLine());
            s = Integer.parseInt(st.nextToken());
            g = Integer.parseInt(st.nextToken());
            h = Integer.parseInt(st.nextToken());

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                int d = Integer.parseInt(st.nextToken());

                edges[a].add(new int[]{b, d});
                edges[b].add(new int[]{a, d});
            }

            set = new HashSet<>();
            for (int i = 0; i < t; i++) {
                int x = Integer.parseInt(br.readLine());
                set.add(x);
            }

            int[] fVisited = new int[n + 1];
            PriorityQueue<int[]> fpq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
            Arrays.fill(fVisited, Integer.MAX_VALUE);
            dijk(fpq, fVisited, s);

            int ns = fVisited[g] > fVisited[h] ? g : h;
            int temp = fVisited[ns];
            int[] sVisited = new int[n + 1];
            Arrays.fill(sVisited, Integer.MAX_VALUE);
            PriorityQueue<int[]> spq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
            dijk(spq, sVisited, ns);

            List<Integer> result = new ArrayList<>();
            for (int node : set) {
                if (sVisited[node] == Integer.MAX_VALUE) continue;
                if (fVisited[node] == sVisited[node] + temp) result.add(node);
            }

            Collections.sort(result);
            for (int node : result) sb.append(node).append(" ");
            sb.append("\n");

        }
        System.out.print(sb);
    }

    private static void dijk(PriorityQueue<int[]> pq, int[] visited, int start) {
        pq.add(new int[]{start, 0});
        while (!pq.isEmpty()) {
            int[] poll = pq.poll();
            int node = poll[0], distance = poll[1];
            if (visited[node] <= distance) continue;
            visited[node] = distance;

            for (int[] edge : edges[node]) {
                int next = edge[0], d = edge[1];
                if (visited[next] <= distance + d) continue;
                pq.add(new int[]{next, distance + d});
            }
        }
    }
}
