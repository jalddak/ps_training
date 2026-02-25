package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_11404 {

    private static int n, m;
    private static int[][] board;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        board = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.MAX_VALUE;
                if (i == j) board[i][j] = 0;
            }
        }

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int f = Integer.parseInt(st.nextToken()) - 1;
            int s = Integer.parseInt(st.nextToken()) - 1;
            int cost = Integer.parseInt(st.nextToken());

            board[f][s] = Math.min(board[f][s], cost);
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (board[i][k] == Integer.MAX_VALUE || board[k][j] == Integer.MAX_VALUE) continue;
                    board[i][j] = Math.min(board[i][j], board[i][k] + board[k][j]);
                }
            }
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == Integer.MAX_VALUE) board[i][j] = 0;
                sb.append(board[i][j]).append(" ");
            }
            sb.append("\n");
        }

        System.out.println(sb);
    }
}