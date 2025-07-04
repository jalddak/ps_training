package ps_traning.swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class No_1961 {
    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= t; tc++) {
            sb.append("#").append(tc).append("\n");
            int n = Integer.valueOf(br.readLine());
            int[][] board = new int[n][n];
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) board[i][j] = Integer.valueOf(st.nextToken());
            }
            solution(n, board);
        }
        System.out.print(sb);
    }

    public static void solution(int n, int[][] board) {
        String[][] result = new String[n][3];
        for (int r = 0; r < 3; r++) {
            int[][] next = new int[n][n];
            for (int i = 0; i < n; i++) {
                StringBuilder row = new StringBuilder();
                for (int j = 0; j < n; j++) {
                    int num = board[n - 1 - j][i];
                    System.out.println(Arrays.toString(board[0]));
                    next[i][j] = num;
                    row.append(num);
                }
                System.out.println(Arrays.toString(next[i]));
                result[i][r] = row.toString();
                row.setLength(0);
            }
            board = next;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < 3; j++) {
                sb.append(result[i][j]).append(" ");
            }
            sb.append("\n");
        }
    }
}
