package ps_traning.algostudy._250925.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_2624 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());

        int[] dp = new int[T + 1];
        dp[0] = 1;

        for (int i = 0; i < k; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());
            int[] next = new int[T + 1];

            int m = 0;
            for (int j = 0; j < p; j++) {
                m += n;

                for (int d = m; d <= T; d++) {
                    next[d] += dp[d - m];
                }
            }

            for (int j = 0; j <= T; j++) {
                next[j] += dp[j];
            }

            dp = next;
        }

        System.out.println(dp[T]);
    }

}