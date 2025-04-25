package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_9465 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.valueOf(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int tc = 0; tc < t; tc++) {
            int n = Integer.valueOf(br.readLine());
            int[][] sts = new int[2][n];

            for (int i = 0; i < 2; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    sts[i][j] = Integer.valueOf(st.nextToken());
                }
            }

            int[] dp = {sts[0][0], sts[1][0], 0};

            for (int i = 1; i < n; i++) {
                int[] temp = {Math.max(dp[1], dp[2]) + sts[0][i]
                        , Math.max(dp[0], dp[2]) + sts[1][i]
                        , Math.max(dp[0], dp[1])};
                dp = temp;
            }

            sb.append(Arrays.stream(dp).max().getAsInt()).append("\n");
        }
        System.out.print(sb.toString());
    }
}
