package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class No_2239 {

    private static int[][] board = new int[9][9];
    private static List<int[]> order = new ArrayList<>();
    private static boolean result = false;


    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 9; i++) {
            char[] input = br.readLine().toCharArray();
            for (int j = 0; j < 9; j++) {
                board[i][j] = input[j] - '0';
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
            bt(depth + 1);
            if (result) break;
            board[y][x] = 0;
        }
    }

    private static boolean check(int y, int x, int num) {
        for (int i = 0; i < 9; i++) {
            if (board[i][x] == num || board[y][i] == num)
                return false;
        }

        int sy = y / 3 * 3;
        int sx = x / 3 * 3;

        for (int i = sy; i < sy + 3; i++) {
            for (int j = sx; j < sx + 3; j++) {
                if (board[i][j] == num) return false;
            }
        }

        return true;
    }
}
