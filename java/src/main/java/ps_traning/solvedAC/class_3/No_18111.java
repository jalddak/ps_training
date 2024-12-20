package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_18111 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken());
        int m = Integer.valueOf(st.nextToken());
        int b = Integer.valueOf(st.nextToken());

        int minH = 256;
        int maxH = 0;
        int[][] board = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int j = 0;
            while (st.hasMoreTokens()) {
                int height = Integer.valueOf(st.nextToken());
                minH = Math.min(minH, height);
                maxH = Math.max(maxH, height);
                b += height;
                board[i][j++] = height;
            }
        }
        maxH = Math.min(maxH, b / (n * m));

        int minC = n * m * 2 * 256;
        for (; minH <= maxH; minH++) {
            int cost = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    int temp = minH - board[i][j];
                    cost += temp >= 0 ? temp : temp * -2;
                }
            }
            if (cost > minC) break;
            minC = cost;
        }
        System.out.println(minC + " " + --minH);
    }
}
