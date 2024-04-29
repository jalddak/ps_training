package ps_traning.programmers.level_2;

public class 멀리_뛰기 {
    public long solution(int n) {
        long answer = 0;
        long[] dp = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            if (i == 1) dp[i] = 1;
            else if (i == 2) dp[i] = 2;
            else dp[i] = (dp[i - 2] + dp[i - 1]) % 1234567;
        }
        answer = dp[n];
        return answer;
    }
}
