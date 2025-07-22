package ps_traning.s14.swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class No_1954 {

    private static StringBuilder sb = new StringBuilder();
    private static int[] dy = {0, 1, 0, -1};
    private static int[] dx = {1, 0, -1, 0};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tcCnt = Integer.valueOf(br.readLine());

        for (int tc = 1; tc <= tcCnt; tc++) {
            int n = Integer.valueOf(br.readLine());
            int y = 0, x = 0, d = 0;
            int[][] board = new int[n][n];
            for (int i = 1; i <= n * n; i++) {
                board[y][x] = i;
                int ny = y + dy[d];
                int nx = x + dx[d];
                if (ny >= n || nx >= n || ny < 0 || nx < 0 || board[ny][nx] != 0) {
                    d = d != 3 ? d + 1 : 0;
                    y += dy[d];
                    x += dx[d];
                    continue;
                }
                y = ny;
                x = nx;
            }
            sb.append("#").append(tc).append("\n");
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    sb.append(board[i][j]).append(" ");
                }
                sb.append("\n");
            }
        }

        System.out.print(sb);
    }
}

