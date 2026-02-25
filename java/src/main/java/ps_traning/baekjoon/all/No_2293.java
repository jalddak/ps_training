package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class No_2293 {

    private static int n, k;
    private static List<Integer> coins = new ArrayList<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            if (num > k) continue;
            coins.add(num);
        }

        int[] dp = new int[k + 1];
        dp[0] = 1;

        for (int coin : coins) {
            for (int i = 1; i <= k; i++) {
                if (i - coin < 0) continue;
                dp[i] = dp[i - coin] + dp[i];
            }
        }

        System.out.println(dp[k]);

    }
}
