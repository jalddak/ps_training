package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_14503 {

    private static int n, m;
    private static int[][] board;
    private static int[] dr = {-1, 0, 1, 0};
    private static int[] dc = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        board = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int result = 0;

        while (true) {
            if (board[r][c] == 0) {
                board[r][c] = 2;
                result++;
                continue;
            }

            boolean flag = false;
            for (int t = 0; t < 4; t++) {
                int ar = r + dr[t];
                int ac = c + dc[t];
                if (board[ar][ac] != 0) continue;
                flag = true;
            }

            if (flag) {
                d = d != 0 ? d - 1 : 3;
                int nr = r + dr[d];
                int nc = c + dc[d];
                if (board[nr][nc] != 0) continue;
                r = nr;
                c = nc;
            } else {
                int nr = r + dr[(d + 2) % 4];
                int nc = c + dc[(d + 2) % 4];
                if (board[nr][nc] == 1) break;
                r = nr;
                c = nc;
            }
        }

        System.out.println(result);
    }
}
