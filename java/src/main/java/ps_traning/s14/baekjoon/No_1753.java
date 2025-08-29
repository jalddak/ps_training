package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class No_1753 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int v = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());

        int start = Integer.parseInt(br.readLine());
        int[] distances = new int[v + 1];
        Arrays.fill(distances, Integer.MAX_VALUE);
        distances[start] = 0;


        Map<Integer, Map<Integer, Integer>> edges = new HashMap<>();
        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            if (!edges.containsKey(a)) edges.put(a, new HashMap<>());
            if (!edges.get(a).containsKey(b)) edges.get(a).put(b, w);
            if (edges.get(a).get(b) > w) edges.get(a).put(b, w);
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            return a[0] - b[0];
        });
        pq.offer(new int[]{distances[start], start});
        while (!pq.isEmpty()) {
            int[] info = pq.poll();
            int d = info[0], node = info[1];
            if (d > distances[node] || !edges.containsKey(node)) continue;
            for (int next : edges.get(node).keySet()) {
                int temp = d + edges.get(node).get(next);
                if (distances[next] < temp) continue;
                distances[next] = temp;
                pq.offer(new int[]{temp, next});
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= v; i++) {
            sb.append(distances[i] == Integer.MAX_VALUE ? "INF" : distances[i]).append("\n");
        }
        System.out.print(sb);
    }
}