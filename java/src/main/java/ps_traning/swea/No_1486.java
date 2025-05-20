package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_1486 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("#").append(tc).append(" ");
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.valueOf(st.nextToken());
            int b = Integer.valueOf(st.nextToken());
            st = new StringTokenizer(br.readLine());
            int[] hs = new int[n];
            for (int i = 0; i < n; i++) {
                hs[i] = Integer.valueOf(st.nextToken());
            }
            Arrays.sort(hs);
            int result = Arrays.stream(hs).sum();
            result = recursion(n, b, hs, 0, 0, result);
            sb.append(result - b).append("\n");
        }
        System.out.print(sb);
    }

    private static int recursion(int n, int b, int[] hs, int start, int cur, int candidate) {
        for (int i = start; i < n; i++) {
            int next = cur + hs[i];
            if (next >= candidate) break;
            if (next < candidate && next >= b) {
                candidate = next;
                break;
            }
            candidate = recursion(n, b, hs, i + 1, next, candidate);
        }

        return candidate;
    }
}
