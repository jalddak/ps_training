package ps_traning.baekjoon.random;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_7453 {

    private static int n;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());

        int[] a = new int[n];
        int[] b = new int[n];
        int[] c = new int[n];
        int[] d = new int[n];
        int[] ab = new int[n * n];
        int[] cd = new int[n * n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            a[i] = Integer.parseInt(st.nextToken());
            b[i] = Integer.parseInt(st.nextToken());
            c[i] = Integer.parseInt(st.nextToken());
            d[i] = Integer.parseInt(st.nextToken());
        }

        int idx = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                ab[idx] = a[i] + b[j];
                cd[idx++] = c[i] + d[j];
            }
        }

        Arrays.sort(ab);
        Arrays.sort(cd);

        long result = 0;
        int s = 0;
        int e = n * n - 1;
        while (s < n * n && e >= 0) {
            int sum = ab[s] + cd[e];
            if (sum > 0) e--;
            else if (sum < 0) s++;
            else {
                long sCnt = 1;
                long eCnt = 1;
                while (s < n * n - 1 && ab[s + 1] == ab[s]) {
                    s++;
                    sCnt++;
                }
                while (e > 0 && cd[e - 1] == cd[e]) {
                    e--;
                    eCnt++;
                }
                s++;
                e--;
                result += sCnt * eCnt;
            }
        }

        System.out.println(result);
    }
}