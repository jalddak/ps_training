package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class No_17626 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());

        int[] dp = new int[n + 1];
        List<Integer> nums = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            double a = Math.sqrt(i);
            if (a == (int) a) {
                nums.add(i);
                dp[i] = 1;
            } else {
                dp[i] = dp[i - 1] + 1;
                for (int num : nums) {
                    dp[i] = Math.min(dp[i - num] + 1, dp[i]);
                }
            }
        }
        System.out.println(dp[n]);
    }
}
