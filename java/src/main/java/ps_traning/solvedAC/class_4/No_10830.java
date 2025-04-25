package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_10830 {
    private static int n;
    private static long b;
    private static int[][] board, answer;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.valueOf(st.nextToken());
        b = Long.valueOf(st.nextToken());

        board = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.valueOf(st.nextToken());
            }
        }

        answer = divide(b);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                sb.append(answer[i][j] % 1000).append(" ");
            }
            sb.append("\n");
        }
        System.out.print(sb.toString());
    }

    private static int[][] divide(long num) {
        if (num == 1) return board;
        long half = num / 2;
        int[][] result = divide(half);
        result = calc(result, result);
        if (num % 2 != 0) result = calc(result, board);
        return result;
    }

    private static int[][] calc(int[][] one, int[][] two) {
        int[][] result = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    result[i][j] += one[i][k] * two[k][j];
                }
                result[i][j] %= 1000;
            }
        }
        return result;
    }
}
