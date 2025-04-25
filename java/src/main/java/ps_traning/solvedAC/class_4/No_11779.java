package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_11779 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int m = Integer.valueOf(br.readLine());

        StringTokenizer st;
        Map<Integer, Integer>[] edges = new HashMap[n + 1];
        for (int i = 0; i <= n; i++) edges[i] = new HashMap<>();
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.valueOf(st.nextToken());
            int e = Integer.valueOf(st.nextToken());
            int cost = Integer.valueOf(st.nextToken());
            if (!edges[s].containsKey(e) || edges[s].get(e) > cost) edges[s].put(e, cost);
        }
        st = new StringTokenizer(br.readLine());
        int s = Integer.valueOf(st.nextToken());
        int e = Integer.valueOf(st.nextToken());

        int[] costs = new int[n + 1];
        Arrays.fill(costs, 100000 * n + 1);
        int[] parents = new int[n + 1];

        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });

        pq.offer(new int[]{0, s});
        costs[s] = 0;

        while (!pq.isEmpty()) {
            int[] pqr = pq.poll();
            int cost = pqr[0], x = pqr[1];
            if (x == e) break;
            if (costs[x] < cost) continue;
            for (int nx : edges[x].keySet()) {
                int nCost = cost + edges[x].get(nx);
                if (costs[nx] <= nCost) continue;
                costs[nx] = nCost;
                parents[nx] = x;
                pq.offer(new int[]{nCost, nx});
            }
        }

        Stack<Integer> result = new Stack<>();
        result.push(e);
        while (parents[result.peek()] != 0) result.push(parents[result.peek()]);

        StringBuilder sb = new StringBuilder();
        sb.append(costs[e]).append("\n");
        sb.append(result.size()).append("\n");
        while (!result.isEmpty()) {
            sb.append(result.pop()).append(" ");
        }
        sb.append("\n");
        System.out.print(sb.toString());
    }
}
