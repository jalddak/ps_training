package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_1247 {
    private static int result, n, hx, hy;
    private static int[][] csInfo;
    private static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            init();
            sb.append("#").append(tc).append(" ");
            n = Integer.valueOf(br.readLine());
            StringTokenizer st = new StringTokenizer(br.readLine());
            int cx = Integer.valueOf(st.nextToken());
            int cy = Integer.valueOf(st.nextToken());
            hx = Integer.valueOf(st.nextToken());
            hy = Integer.valueOf(st.nextToken());
            csInfo = new int[n][2];
            for (int i = 0; i < n; i++) {
                int x = Integer.valueOf(st.nextToken());
                int y = Integer.valueOf(st.nextToken());
                csInfo[i][0] = x;
                csInfo[i][1] = y;
            }
            visited = new boolean[n];
            dfs(0, cx, cy, 0);
            sb.append(result).append("\n");
        }
        System.out.print(sb);
    }

    private static void dfs(int depth, int bx, int by, int preSum) {
        if (preSum >= result) return;
        if (depth == n) {
            result = Math.min(result, preSum + Math.abs(bx - hx) + Math.abs(by - hy));
            return;
        }

        for (int i = 0; i < n; i++) {
            if (visited[i]) continue;
            visited[i] = true;
            int nx = csInfo[i][0], ny = csInfo[i][1];
            int nPreSum = preSum + Math.abs(bx - nx) + Math.abs(by - ny);
            dfs(depth + 1, nx, ny, nPreSum);
            visited[i] = false;
        }


    }

    private static void init() {
        result = 10000;
        n = 0;
        hx = 0;
        hy = 0;
        csInfo = new int[n][2];
        visited = new boolean[n];
    }
}
