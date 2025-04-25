package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_1916_Map {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int m = Integer.valueOf(br.readLine());
        StringTokenizer st;
        Map<Integer, Map<Integer, Integer>> costs = new HashMap<>();
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.valueOf(st.nextToken());
            int e = Integer.valueOf(st.nextToken());
            int cost = Integer.valueOf(st.nextToken());
            if (!costs.containsKey(s)) {
                Map<Integer, Integer> ecost = new HashMap<>();
                ecost.put(e, cost);
                costs.put(s, ecost);
            } else if (!costs.get(s).containsKey(e) || costs.get(s).get(e) > cost) {
                costs.get(s).put(e, cost);
            }
        }

        st = new StringTokenizer(br.readLine());
        int s = Integer.valueOf(st.nextToken());
        int e = Integer.valueOf(st.nextToken());

        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });
        pq.add(new int[]{0, s});
        int[] check = new int[n + 1];
        Arrays.fill(check, 100000001);
        check[s] = 0;

        while (!pq.isEmpty()) {
            int[] pqr = pq.poll();
            int cost = pqr[0], x = pqr[1];
            if (x == e) {
                System.out.println(cost);
                break;
            }
            if (cost > check[x] || !costs.containsKey(x)) continue;
            for (int nx : costs.get(x).keySet()) {
                int nCost = cost + costs.get(x).get(nx);
                if (nCost >= check[nx]) continue;
                pq.offer(new int[]{nCost, nx});
                check[nx] = nCost;
            }
        }
    }
}
