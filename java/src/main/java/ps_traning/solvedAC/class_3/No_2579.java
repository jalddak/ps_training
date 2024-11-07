package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class No_2579 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int[] stairs = new int[n];
        for (int i = 0; i < n; i++) {
            stairs[i] = Integer.valueOf(br.readLine());
        }
        if (n == 1) {
            System.out.println(stairs[0]);
            System.exit(0);
        }

        int[][] dp = new int[n][2];
        dp[0] = new int[]{stairs[0], 0};
        dp[1] = new int[]{stairs[1], stairs[0] + stairs[1]};
        for (int i = 2; i < n; i++) {
            dp[i][0] = Math.max(dp[i - 2][0], dp[i - 2][1]) + stairs[i];
            dp[i][1] = dp[i - 1][0] + stairs[i];
        }
        System.out.println(Arrays.stream(dp[n - 1]).max().getAsInt());
    }
}
