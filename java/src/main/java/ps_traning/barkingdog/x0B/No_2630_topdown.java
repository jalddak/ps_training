package ps_traning.barkingdog.x0B;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_2630_topdown {

    private static int n;
    private static int[][] board;
    private static int[] answer = new int[2];
    private static int[] dy = {0, 0, 1, 1};
    private static int[] dx = {0, 1, 0, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.valueOf(br.readLine());
        board = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.valueOf(st.nextToken());
            }
        }

        rc(n, 0, 0);
        for (int a : answer) System.out.println(a);
    }

    private static void rc(int l, int y, int x) {
        if (l == 1) {
            answer[board[y][x]] += 1;
            return;
        }

        boolean flag = true;
        int temp = board[y][x];
        for (int i = 0; i < l; i++) {
            for (int j = 0; j < l; j++) {
                int ay = y + i;
                int ax = x + j;
                if (temp != board[ay][ax]) {
                    flag = false;
                    break;
                }
            }
            if (!flag) break;
        }

        if (flag) answer[board[y][x]] += 1;
        else {
            int nl = l / 2;
            for (int d = 0; d < 4; d++) {
                int ny = y + dy[d] * nl;
                int nx = x + dx[d] * nl;
                rc(nl, ny, nx);
            }
        }
    }
}
