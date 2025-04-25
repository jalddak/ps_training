package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class No_1216 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = 10;

        for (int tc = 1; tc <= tcCnt; tc++) {
            int tcNum = Integer.valueOf(br.readLine());
            sb.append("#").append(tcNum).append(" ");

            char[][] board = new char[200][100];

            int result = 0;
            for (int i = 0; i < 100; i++) {
                char[] row = br.readLine().toCharArray();
                board[i] = row;
                for (int j = 0; j < 100; j++) {
                    board[100 + j][i] = board[i][j];
                }
            }

            for (int i = 0; i < 200; i++) {
                result = Math.max(result, dp(board[i]));
            }

            sb.append(result).append("\n");
        }
        System.out.print(sb);
    }

    private static int dp(char[] row) {
        boolean[][] dp = new boolean[100][100];
        for (int i = 0; i < 100; i++) {
            Arrays.fill(dp[i], true);
        }

        int result = 0;
        for (int i = 1; i < 99; i++) {
            for (int j = 0; j < 100 - i; j++) {
                if (row[j] != row[j + i] || !dp[j + 1][j + i - 1]) {
                    dp[j][j + i] = false;
                    continue;
                }
                result = Math.max(result, i + 1);
            }
        }
        return result;
    }
}
