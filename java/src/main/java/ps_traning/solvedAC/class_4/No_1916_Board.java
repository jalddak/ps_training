package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class No_1916_Board {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int m = Integer.valueOf(br.readLine());
        StringTokenizer st;

        int[][] costs = new int[n + 1][n + 1];
        for (int i = 0; i <= n; i++) {
            Arrays.fill(costs[i], 100001);
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.valueOf(st.nextToken());
            int e = Integer.valueOf(st.nextToken());
            int cost = Integer.valueOf(st.nextToken());
            costs[s][e] = costs[s][e] > cost ? cost : costs[s][e];
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
            if (cost > check[x]) continue;
            for (int nx = 1; nx <= n; nx++) {
                if (nx == x || costs[x][nx] > 100000) continue;
                int nCost = cost + costs[x][nx];
                if (nCost >= check[nx]) continue;
                pq.offer(new int[]{nCost, nx});
                check[nx] = nCost;
            }
        }
    }
}
