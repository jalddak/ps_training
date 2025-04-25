package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class No_12851 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken());
        int k = Integer.valueOf(st.nextToken());

        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[0] - o2[0];
            }
        });
        int[][] checked = new int[100001][2];
        pq.offer(new int[]{0, n});
        for (int i = 0; i <= 100000; i++) {
            if (i == n) {
                checked[i][1] = 1;
                continue;
            }
            checked[i][0] = 100001;
            checked[i][1] = 0;
        }

        while (!pq.isEmpty()) {
            int[] pqr = pq.poll();
            int t = pqr[0], x = pqr[1];
            if (checked[x][0] < t) continue;
            int[] move = {x - 1, x + 1, 2 * x};
            int nt = t + 1;
            for (int nx : move) {
                if (nx > 100000 || nx < 0 || checked[nx][0] < nt || checked[k][0] < nt + nx - k) continue;
                if (checked[nx][0] == nt) checked[nx][1]++;
                else {
                    checked[nx][0] = nt;
                    checked[nx][1] = 1;
                }
                pq.offer(new int[]{nt, nx});
            }
        }

        System.out.println(checked[k][0]);
        System.out.println(checked[k][1]);
    }
}
