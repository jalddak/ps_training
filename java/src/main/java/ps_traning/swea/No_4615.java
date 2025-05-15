package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_4615 {
    private static int[] dy = {-1, -1, -1, 0, 1, 1, 1, 0};
    private static int[] dx = {-1, 0, 1, 1, 1, 0, -1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("#").append(tc).append(" ");
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.valueOf(st.nextToken());
            int m = Integer.valueOf(st.nextToken());
            int[][] board = new int[n][n];
            int half = n / 2;
            board[half - 1][half - 1] = 2;
            board[half][half - 1] = 1;
            board[half - 1][half] = 1;
            board[half][half] = 2;

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.valueOf(st.nextToken()) - 1;
                int y = Integer.valueOf(st.nextToken()) - 1;
                int k = Integer.valueOf(st.nextToken());

                for (int d = 0; d < 8; d++) {
                    int ny = y + dy[d];
                    int nx = x + dx[d];
                    dfs(board, n, ny, nx, k, d);
                }
                board[y][x] = k;
            }

            int black = 0;
            int white = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (board[i][j] == 1) black++;
                    if (board[i][j] == 2) white++;
                }
            }
            sb.append(black).append(" ").append(white).append("\n");
        }
        System.out.print(sb);
    }

    private static boolean dfs(int[][] board, int n, int y, int x, int k, int d) {
        if (y >= n || y < 0 || x >= n || x < 0 || board[y][x] == 0) return false;
        if (board[y][x] == k) return true;
        boolean result = dfs(board, n, y + dy[d], x + dx[d], k, d);
        if (result) board[y][x] = k;
        return result;
    }
}
