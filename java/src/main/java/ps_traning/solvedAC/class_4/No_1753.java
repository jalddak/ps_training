package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_1753 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int v = Integer.valueOf(st.nextToken());
        int e = Integer.valueOf(st.nextToken());
        int k = Integer.valueOf(br.readLine());


        Map<Integer, Map<Integer, Integer>> edges = new HashMap<>();
        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.valueOf(st.nextToken());
            int end = Integer.valueOf(st.nextToken());
            int weight = Integer.valueOf(st.nextToken());

            if (!edges.containsKey(start)) {
                Map<Integer, Integer> edge = new HashMap<>();
                edge.put(end, weight);
                edges.put(start, edge);
            } else if (!edges.get(start).containsKey(end) || edges.get(start).get(end) > weight) {
                edges.get(start).put(end, weight);
            }
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });

        pq.offer(new int[]{0, k});
        int[] checked = new int[v + 1];
        Arrays.fill(checked, 20000 * 10 + 1);
        checked[k] = 0;

        while (!pq.isEmpty()) {
            int[] pqr = pq.poll();
            int w = pqr[0], x = pqr[1];
            if (w > checked[x] || !edges.containsKey(x)) continue;
            for (int nx : edges.get(x).keySet()) {
                int nw = w + edges.get(x).get(nx);
                if (nw >= checked[nx]) continue;
                checked[nx] = nw;
                pq.offer(new int[]{nw, nx});
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= v; i++) {
            if (checked[i] == 20000 * 10 + 1) sb.append("INF\n");
            else sb.append(checked[i]).append("\n");
        }
        System.out.print(sb.toString());

    }
}
