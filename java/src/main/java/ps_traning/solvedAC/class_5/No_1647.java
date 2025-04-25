package ps_traning.solvedAC.class_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_1647 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken());
        int m = Integer.valueOf(st.nextToken());
        Map<Integer, Integer>[] edges = new HashMap[n + 1];
        for (int i = 0; i <= n; i++) {
            edges[i] = new HashMap<>();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.valueOf(st.nextToken());
            int b = Integer.valueOf(st.nextToken());
            int c = Integer.valueOf(st.nextToken());

            if (!edges[a].containsKey(b) || edges[a].get(b) > c) {
                edges[a].put(b, c);
                edges[b].put(a, c);
            }
        }

        int answer = 0;
        int maxCost = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });
        pq.add(new int[]{0, 1});

        Set<Integer> visited = new HashSet<>();

        while (!pq.isEmpty() && visited.size() < n) {
            int[] pqr = pq.poll();
            int cost = pqr[0], node = pqr[1];
            if (visited.contains(node)) continue;
            visited.add(node);
            answer += cost;
            maxCost = Math.max(cost, maxCost);

            for (int nNode : edges[node].keySet()) {
                if (visited.contains(nNode)) continue;
                int nCost = edges[node].get(nNode);
                pq.add(new int[]{nCost, nNode});
            }
        }

        answer -= maxCost;
        System.out.println(answer);

    }
}
