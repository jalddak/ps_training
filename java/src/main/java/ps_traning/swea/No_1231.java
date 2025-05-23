package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_1231 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = 10;
        for (int tc = 1; tc <= tcCnt; tc++) {
            int n = Integer.valueOf(br.readLine());
            String[] arr = new String[n + 1];
            int[][] childs = new int[n + 1][2];
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int node = Integer.valueOf(st.nextToken());
                arr[node] = st.nextToken();
                if (st.hasMoreTokens()) childs[node][0] = Integer.valueOf(st.nextToken());
                if (st.hasMoreTokens()) childs[node][1] = Integer.valueOf(st.nextToken());
            }

            String result = recursion(arr, childs, 1);
            sb.append("#").append(tc).append(" ").append(result).append("\n");
        }
        System.out.print(sb);
    }

    private static String recursion(String[] arr, int[][] childs, int node) {
        StringBuilder sb = new StringBuilder();
        if (childs[node][0] != 0) sb.append(recursion(arr, childs, childs[node][0]));
        sb.append(arr[node]);
        if (childs[node][1] != 0) sb.append(recursion(arr, childs, childs[node][1]));
        return sb.toString();
    }
}
