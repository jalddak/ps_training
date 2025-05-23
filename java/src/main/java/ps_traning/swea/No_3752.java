package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_3752 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            int n = Integer.valueOf(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] scores = new int[n];
            for (int i = 0; i < n; i++) {
                scores[i] = Integer.valueOf(st.nextToken());
            }
            int allSum = Arrays.stream(scores).sum();
            boolean[] dp = new boolean[allSum + 1];
            dp[0] = true;

            for (int score : scores) {
                for (int i = allSum; i >= score; i--) {
                    if (dp[i - score]) dp[i] = true;
                }
            }

            int result = 0;
            for (int i = 0; i <= allSum; i++) {
                if (dp[i]) result++;
            }
            sb.append("#").append(tc).append(" ").append(result).append("\n");
        }
        System.out.print(sb);
    }
}
