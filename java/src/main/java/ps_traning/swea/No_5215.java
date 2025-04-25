package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_5215 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("#").append(tc).append(" ");
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.valueOf(st.nextToken());
            int l = Integer.valueOf(st.nextToken());
            int[] dp = new int[l + 1];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                int t = Integer.valueOf(st.nextToken());
                int k = Integer.valueOf(st.nextToken());
                for (int j = l; j >= k; j--) {
                    dp[j] = Math.max(dp[j], dp[j - k] + t);
                }
            }

            sb.append(dp[l]).append("\n");
        }
        System.out.print(sb);
    }
}
