package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_1916_List {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int m = Integer.valueOf(br.readLine());
        StringTokenizer st;

        List<int[]>[] costs = new ArrayList[n + 1];
        for (int i = 0; i <= n; i++) {
            costs[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.valueOf(st.nextToken());
            int e = Integer.valueOf(st.nextToken());
            int cost = Integer.valueOf(st.nextToken());
            costs[s].add(new int[]{e, cost});
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
            for (int[] costsInfo : costs[x]) {
                int nx = costsInfo[0], plus = costsInfo[1];
                int nCost = cost + plus;
                if (nCost >= check[nx]) continue;
                pq.offer(new int[]{nCost, nx});
                check[nx] = nCost;
            }
        }
    }
}
