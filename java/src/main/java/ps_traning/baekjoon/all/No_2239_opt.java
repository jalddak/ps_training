package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class No_2239_opt {

    private static int[][] board = new int[9][9];
    private static List<int[]> order = new ArrayList<>();
    private static boolean result = false;
    private static boolean[][] rowCheck = new boolean[9][10];
    private static boolean[][] colCheck = new boolean[9][10];
    private static boolean[][] boxCheck = new boolean[9][10];

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 9; i++) {
            char[] input = br.readLine().toCharArray();
            for (int j = 0; j < 9; j++) {
                board[i][j] = input[j] - '0';
                rowCheck[i][board[i][j]] = true;
                colCheck[j][board[i][j]] = true;
                boxCheck[(i / 3 * 3) + (j / 3)][board[i][j]] = true;
                if (board[i][j] != 0) continue;
                order.add(new int[]{i, j});
            }
        }

        bt(0);
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                sb.append(board[i][j]);
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }

    private static void bt(int depth) {
        if (depth == order.size()) {
            result = true;
            return;
        }

        for (int i = 1; i <= 9; i++) {
            int[] cd = order.get(depth);
            int y = cd[0], x = cd[1];
            if (!check(y, x, i)) continue;
            board[y][x] = i;
            rowCheck[y][board[y][x]] = true;
            colCheck[x][board[y][x]] = true;
            boxCheck[(y / 3 * 3) + (x / 3)][board[y][x]] = true;
            bt(depth + 1);
            if (result) break;
            rowCheck[y][board[y][x]] = false;
            colCheck[x][board[y][x]] = false;
            boxCheck[(y / 3 * 3) + (x / 3)][board[y][x]] = false;
            board[y][x] = 0;
        }
    }

    private static boolean check(int y, int x, int num) {
        return !(rowCheck[y][num] || colCheck[x][num] || boxCheck[y / 3 * 3 + x / 3][num]);
    }
}
