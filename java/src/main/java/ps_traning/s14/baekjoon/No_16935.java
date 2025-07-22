package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_16935 {

    private static int r;
    private static int[][] board;
    private static int[][] result;
    private static int[] cmds;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.valueOf(st.nextToken());
        int m = Integer.valueOf(st.nextToken());
        r = Integer.valueOf(st.nextToken());

        board = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.valueOf(st.nextToken());
            }
        }

        cmds = new int[r];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < r; i++) cmds[i] = Integer.valueOf(st.nextToken());
        for (int cmd : cmds) {
            switch (cmd) {
                case 1:
                    one();
                    break;
                case 2:
                    two();
                    break;
                case 3:
                    three();
                    break;
                case 4:
                    four();
                    break;
                case 5:
                    five();
                    break;
                case 6:
                    six();
                    break;
            }
            board = result;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.length; i++) {
            for (int j = 0; j < result[i].length; j++) {
                sb.append(result[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.print(sb);
    }

    private static void one() {
        int n = board.length;
        int m = board[0].length;
        for (int i = 0; i < n / 2; i++) {
            for (int j = 0; j < m; j++) {
                int temp = board[i][j];
                board[i][j] = board[n - i - 1][j];
                board[n - i - 1][j] = temp;
            }
        }
        result = board;
    }

    private static void two() {
        int n = board.length;
        int m = board[0].length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m / 2; j++) {
                int temp = board[i][j];
                board[i][j] = board[i][m - j - 1];
                board[i][m - j - 1] = temp;
            }
        }
        result = board;
    }

    private static void three() {
        int n = board.length;
        int m = board[0].length;
        result = new int[m][n];
        for (int i = n - 1; i >= 0; i--) {
            for (int j = 0; j < m; j++) {
                result[j][n - i - 1] = board[i][j];
            }
        }
    }

    private static void four() {
        int n = board.length;
        int m = board[0].length;
        result = new int[m][n];
        for (int i = 0; i < n; i++) {
            for (int j = m - 1; j >= 0; j--) {
                result[m - j - 1][i] = board[i][j];
            }
        }
    }

    private static void five() {
        int[] dy = {0, 1, 0, -1};
        int[] dx = {1, 0, -1, 0};
        fiveSixBase(dy, dx);
    }

    private static void six() {
        int[] dy = {1, 0, -1, 0};
        int[] dx = {0, 1, 0, -1};
        fiveSixBase(dy, dx);
    }

    private static void fiveSixBase(int[] dy, int[] dx) {

        int n = board.length / 2;
        int m = board[0].length / 2;
        int y = 0, x = 0;

        int[][] part = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                part[i][j] = board[i][j];
            }
        }

        for (int d = 0; d < 4; d++) {
            int ny = y + dy[d] * n;
            int nx = x + dx[d] * m;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    int temp = board[ny + i][nx + j];
                    board[ny + i][nx + j] = part[i][j];
                    part[i][j] = temp;
                }
            }
            y = ny;
            x = nx;
        }
        result = board;
    }
}
