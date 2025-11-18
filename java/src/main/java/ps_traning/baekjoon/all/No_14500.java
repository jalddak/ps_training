package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_14500 {

    private static int n, m, result;
    private static int[][] board;
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                recursion(0, -1, 0, i, j);
            }
        }

        System.out.println(result);
    }

    private static void recursion(int depth, int before, int temp, int y, int x) {
        if (depth == 4) {
            result = Math.max(result, temp);
            return;
        }

        if (depth == 2) {
            for (int i = 0; i < 4; i++) {
                if (i == before) continue;
                int ay = y + dy[i];
                int ax = x + dx[i];
                if (ay >= n || ax >= m || ay < 0 || ax < 0) continue;
                for (int j = i + 1; j < 4; j++) {
                    if (j == before) continue;
                    int by = y + dy[j];
                    int bx = x + dx[j];
                    if (by >= n || bx >= m || by < 0 || bx < 0) continue;

                    result = Math.max(result, temp + board[ay][ax] + board[by][bx]);
                }
            }
        }

        for (int d = 0; d < 4; d++) {
            if (d == before) continue;
            int ny = y + dy[d];
            int nx = x + dx[d];
            if (ny >= n || nx >= m || ny < 0 || nx < 0) continue;
            recursion(depth + 1, (d + 2) % 4, temp + board[ny][nx], ny, nx);

        }
    }
}
