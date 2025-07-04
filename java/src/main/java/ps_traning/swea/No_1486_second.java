package ps_traning.swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class No_1486_second {

    private static StringBuilder sb = new StringBuilder();
    private static int n, b, result;
    private static int[] hs;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= t; tc++) {
            sb.append("#").append(tc).append(" ");
            StringTokenizer st = new StringTokenizer(br.readLine());
            n = Integer.valueOf(st.nextToken());
            b = Integer.valueOf(st.nextToken());

            hs = new int[n];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) hs[i] = Integer.valueOf(st.nextToken());
            Arrays.sort(hs);
            result = Arrays.stream(hs).sum();
            dfs(0, 0);
            sb.append(result - b).append("\n");
        }
        System.out.print(sb);
    }

    private static void dfs(int start, int cur) {
        for (int i = start; i < n; i++) {
            int next = cur + hs[i];
            if (next >= result) break;
            if (next >= b) {
                result = next;
                break;
            }
            dfs(i + 1, next);
        }
    }
}