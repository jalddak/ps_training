package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_1106 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int c = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int[][] info = new int[n][2];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 2; j++) info[i][j] = Integer.parseInt(st.nextToken());
        }

        int[] dp = new int[c + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        for (int i = 1; i <= c; i++) {
            for (int j = 0; j < n; j++) {
                if (info[j][1] > i) continue;
                dp[i] = Math.min(dp[i], dp[i - info[j][1]] + info[j][0]);
                for (int k = i - info[j][1] + 1; k < i; k++) {
                    dp[k] = Math.min(dp[k], dp[i]);
                }
            }
        }

        for (int i = 0; i < n; i++) {
            if (info[i][1] <= c) continue;
            dp[c] = Math.min(dp[c], info[i][0]);
        }

        System.out.println(dp[c]);
    }
}
