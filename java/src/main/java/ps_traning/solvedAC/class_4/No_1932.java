package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_1932 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int[] dp;
        dp = new int[]{Integer.valueOf(br.readLine())};

        for (int i = 1; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] temp = new int[i + 1];
            for (int j = 0; j <= i; j++) {
                temp[j] = Integer.valueOf(st.nextToken());
                if (j == 0) temp[j] += dp[0];
                else if (j == i) temp[j] += dp[j - 1];
                else temp[j] += Math.max(dp[j - 1], dp[j]);
            }
            dp = temp;
        }
        System.out.println(Arrays.stream(dp).max().getAsInt());
    }
}
