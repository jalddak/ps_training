package ps_traning.solvedAC.class_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_10942 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int[] nums = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.valueOf(st.nextToken());
        }

        boolean[][] dp = new boolean[n][n];
        dp[n - 1][n - 1] = true;
        for (int i = 0; i < n - 1; i++) {
            dp[i][i] = true;
            if (nums[i] == nums[i + 1]) dp[i][i + 1] = true;
        }

        for (int j = 2; j < n; j++) {
            for (int i = 0; i < n - j; i++) {
                if (nums[i] == nums[i + j] && dp[i + 1][i + j - 1]) dp[i][i + j] = true;
            }
        }

        StringBuilder sb = new StringBuilder();
        int m = Integer.valueOf(br.readLine());
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.valueOf(st.nextToken()) - 1;
            int e = Integer.valueOf(st.nextToken()) - 1;
            sb.append(dp[s][e] ? 1 : 0).append("\n");
        }
        System.out.print(sb.toString());
    }
}
