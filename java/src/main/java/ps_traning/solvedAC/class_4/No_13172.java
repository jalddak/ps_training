package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_13172 {
    private static long mod = 1000000007;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.valueOf(br.readLine());

        long answer = 0;
        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            long n = Long.valueOf(st.nextToken());
            long s = Long.valueOf(st.nextToken());
            long nsGcd = gcd(n, s);
            n /= nsGcd;
            s /= nsGcd;
            answer += s * divide(n, mod - 2) % mod;
            answer %= mod;
        }
        System.out.println(answer);

    }

    private static long gcd(long a, long b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    private static long divide(long num, long power) {
        if (power == 1) return num;
        long result = divide(num, power / 2);
        result = result * result % mod;
        if (power % 2 != 0) result = result * num % mod;
        return result;
    }
}
