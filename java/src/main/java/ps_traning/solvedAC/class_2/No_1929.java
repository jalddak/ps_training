package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_1929 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] mn = new int[2];
        int i = 0;
        while (st.hasMoreTokens()) mn[i++] = Integer.valueOf(st.nextToken());
        int m = mn[0];
        int n = mn[1];
        boolean[] check = new boolean[n + 1];
        Arrays.fill(check, true);
        check[0] = false;
        check[1] = false;

        StringBuilder sb = new StringBuilder();
        for (i = 2; i <= n; i++) {
            if (check[i]) {
                if (i >= m) sb.append(i + "\n");
                for (int j = 2 * i; j <= n; j += i) {
                    check[j] = false;
                }
            }
        }
        System.out.println(sb.toString());
    }
}
