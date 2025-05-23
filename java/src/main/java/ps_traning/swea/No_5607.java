package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_5607 {
    private static long[] dp = new long[1000001];
    private static int mod = 1234567891;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        dp[0] = 1;
        dp[1] = 1;
        for (int i = 2; i < dp.length; i++) {
            dp[i] = dp[i - 1] * i % mod;
        }

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.valueOf(st.nextToken());
            int r = Integer.valueOf(st.nextToken());

            long temp = dp[r] * dp[n - r] % mod;
            long result = dp[n] * pow(temp, mod - 2) % mod;
            sb.append("#").append(tc).append(" ").append(result).append("\n");
        }
        System.out.print(sb);
    }

    private static long pow(long num, int exp) {
        if (exp == 0) return 1;
        if (exp == 1) return num;
        long result = pow(num, exp / 2);
        result = result * result % mod;
        if (exp % 2 != 0) result = result * num % mod;
        return result;
    }
}
