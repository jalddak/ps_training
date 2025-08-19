package ps_traning.codeforce;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class No_337_C {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int a = n - m;
        int b = n / k;
        int c = Math.max(b - a, 0);
        long answer = 0;

        answer = ((k * 2L) * (recursion(c) - 1)) % 1000000009;

        int d = m - c * k;
        answer = (answer + d) % 1000000009;

        sb.append(answer).append("\n");
        System.out.print(sb);
    }

    private static long recursion(int n) {
        if (n == 0) return 1;
        if (n == 1) return 2;
        long temp = recursion(n / 2);
        long result = (temp * temp) % 1000000009;
        if (n % 2 == 1) result = (result * 2) % 1000000009;
        return result;
    }
}

