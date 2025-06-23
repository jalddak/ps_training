package ps_traning.barkingdog.x0B;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_1992 {
    private static int n;
    private static int[][] board;
    private static int[] dy = {0, 0, 1, 1};
    private static int[] dx = {0, 1, 0, 1};
    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.valueOf(br.readLine());
        board = new int[n][n];
        for (int i = 0; i < n; i++) {
            board[i] = br.readLine().chars().map(x -> x - '0').toArray();
        }

        rc(n, 0, 0);
        System.out.print(sb);
    }

    private static void rc(int l, int y, int x) {
        boolean flag = true;
        int temp = board[y][x];
        for (int i = 0; i < l; i++) {
            for (int j = 0; j < l; j++) {
                int ty = y + i;
                int tx = x + j;
                if (board[ty][tx] != temp) {
                    flag = false;
                    break;
                }
            }
            if (!flag) break;
        }

        if (flag) {
            sb.append(board[y][x]);
            return;
        }

        sb.append("(");
        int nl = l / 2;
        for (int d = 0; d < 4; d++) {
            int ny = y + dy[d] * nl;
            int nx = x + dx[d] * nl;
            rc(nl, ny, nx);
        }
        sb.append(")");
    }
}
