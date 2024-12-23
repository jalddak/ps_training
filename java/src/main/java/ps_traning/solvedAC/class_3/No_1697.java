package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_1697 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken());
        int k = Integer.valueOf(st.nextToken());

        if (n == k) {
            System.out.println(0);
            System.exit(0);
        }

        int[] row = new int[100001];
        Arrays.fill(row, 100001);
        row[n] = 0;
        Queue<int[]> q = new LinkedList<>(List.of(new int[]{n, 0}));
        while (!q.isEmpty()) {
            int[] xt = q.poll();
            int x = xt[0], t = xt[1];
            int[] nxs = {x - 1, x + 1, x * 2};
            int nt = t + 1;
            for (int nx : nxs) {
                if (nx == k) {
                    System.out.println(nt);
                    System.exit(0);
                }
                if (nx >= 0 && nx <= 100000 && row[nx] > nt) {
                    row[nx] = nt;
                    q.offer(new int[]{nx, nt});
                }
            }
        }
    }
}
