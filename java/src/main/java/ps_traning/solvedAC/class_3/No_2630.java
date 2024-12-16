package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_2630 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int[][] board = new int[n][n];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int j = 0;
            while (st.hasMoreTokens()) board[i][j++] = Integer.valueOf(st.nextToken());
        }
        int[] result = {0, 0};
        check(board, n, 0, 0, result);
        for (int r : result) {
            System.out.println(r);
        }
    }

    public static void check(int[][] board, int n, int x, int y, int[] result) {
        boolean flag = true;
        int before = board[y][x];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (before != board[y + i][x + j]) {
                    flag = false;
                    break;
                }
            }
            if (!flag) break;
        }
        if (flag) result[board[y][x]] += 1;
        else {
            check(board, n / 2, x, y, result);
            check(board, n / 2, x + n / 2, y, result);
            check(board, n / 2, x, y + n / 2, result);
            check(board, n / 2, x + n / 2, y + n / 2, result);
        }
    }
}
