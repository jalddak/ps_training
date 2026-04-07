package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class No_4811 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        long[][] dp = new long[31][31];

        for (int h = 0; h <= 30; h++) {
            for (int w = 1; w <= 30; w++) {
                if (h == 0) {
                    dp[w][h] = 1;
                    continue;
                }
                if (w > h) {
                    dp[w][h] += dp[w - 1][h];
                }
                dp[w][h] += dp[w][h - 1];
            }
        }

        StringBuilder sb = new StringBuilder();
        while (true) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0) break;
            sb.append(dp[n][n]).append("\n");
        }
        System.out.println(sb);
    }
}
