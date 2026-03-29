package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class No_2725 {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int c = Integer.parseInt(br.readLine());

        int[] candidate = new int[c];

        int maxN = 0;
        for (int i = 0; i < c; i++) {
            candidate[i] = Integer.parseInt(br.readLine());
            maxN = Math.max(maxN, candidate[i]);
        }

        int[] result = new int[maxN + 1];
        result[0] = 0;
        result[1] = 1;

        for (int n = 2; n <= maxN; n++) {
            result[n] += result[n - 1];
            for (int x = 1; x < n; x++) {
                if (gcd(x, n) == 1) result[n]++;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int num : candidate) {
            sb.append(result[num] * 2 + 1).append("\n");
        }
        System.out.println(sb);
    }

    private static int gcd(int n, int m) {
        if (m == 0) return n;
        return gcd(m, n % m);
    }
}
