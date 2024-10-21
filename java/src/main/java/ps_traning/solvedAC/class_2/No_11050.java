package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_11050 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] nk = new int[2];
        int index = 0;
        while (st.hasMoreTokens()) nk[index++] = Integer.valueOf(st.nextToken());

        int[] dp = new int[nk[0] + 1];
        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i <= nk[0]; i++) {
            dp[i] = dp[i - 1] * i;
        }

        int answer = (dp[nk[0]] / (dp[nk[0] - nk[1]] * dp[nk[1]]));
        System.out.println(answer);
    }
}
