package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class No_1504 {
    private static int n, e, m1, m2;
    private static int[][] board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.valueOf(st.nextToken());
        e = Integer.valueOf(st.nextToken());
        board = new int[n + 1][n + 1];
        for (int i = 0; i <= n; i++) {
            Arrays.fill(board[i], 1001);
        }

        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.valueOf(st.nextToken());
            int end = Integer.valueOf(st.nextToken());
            int cost = Integer.valueOf(st.nextToken());

            if (board[start][end] <= cost) continue;
            board[start][end] = cost;
            board[end][start] = cost;
        }

        st = new StringTokenizer(br.readLine());
        m1 = Integer.valueOf(st.nextToken());
        m2 = Integer.valueOf(st.nextToken());


        int a1 = checkResult(m1, m2);
        int a2 = checkResult(m2, m1);
        int answer = a1 != -1 && a2 != -1 ? Math.min(a1, a2) : Math.max(a1, a2);
        System.out.println(answer);
    }

    private static int dijkstra(int start, int end) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });
        pq.offer(new int[]{0, start});
        int[] checked = new int[n + 1];
        Arrays.fill(checked, 1000 * 800 + 1);
        checked[start] = 0;

        while (!pq.isEmpty()) {
            int[] pqr = pq.poll();
            int cost = pqr[0], x = pqr[1];
            if (x == end) return cost;
            if (cost > checked[x]) continue;
            for (int nx = 1; nx <= n; nx++) {
                int nCost = cost + board[x][nx];
                if (nx == x || board[x][nx] == 1001 || nCost >= checked[nx]) continue;
                checked[nx] = nCost;
                pq.offer(new int[]{nCost, nx});
            }
        }

        return -1;
    }

    private static int checkResult(int middle1, int middle2) {
        int r1 = dijkstra(1, middle1);
        int r2 = dijkstra(middle1, middle2);
        int r3 = dijkstra(middle2, n);
        int result = r1 == -1 || r2 == -1 || r3 == -1 ? -1 : r1 + r2 + r3;
        return result;
    }
}
