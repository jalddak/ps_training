package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_17070 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.valueOf(br.readLine());

        int[][] board = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.valueOf(st.nextToken());
            }
        }

        int[][][] dp = new int[n][n][3];
        for (int i = 1; i < n; i++) {
            if (board[0][i] == 1) break;
            dp[0][i] = new int[]{1, 0, 0};
        }

        for (int i = 1; i < n; i++) {
            for (int j = 2; j < n; j++) {
                if (board[i][j] == 1) continue;
                int n1 = dp[i][j - 1][0] + dp[i][j - 1][2];
                int n2 = dp[i - 1][j][1] + dp[i - 1][j][2];
                int n3 = board[i][j - 1] == 1 || board[i - 1][j] == 1 ? 0 : Arrays.stream(dp[i - 1][j - 1]).sum();
                dp[i][j] = new int[]{n1, n2, n3};
            }
        }

        System.out.println(Arrays.stream(dp[n - 1][n - 1]).sum());

    }
}
