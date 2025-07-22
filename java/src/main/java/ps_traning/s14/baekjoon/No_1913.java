package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class No_1913 {

    private static int n;
    private static int[][] board;
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int s = Integer.valueOf(br.readLine());

        board = new int[n][n];
        int y = n / 2, x = n / 2;
        int num = 1;
        board[y][x] = num++;
        int cnt = 1;
        int check = 0;
        int d = 0;

        while (num < n * n) {
            for (int i = 0; i < cnt; i++) {
                y = y + dy[d];
                x = x + dx[d];
                board[y][x] = num++;
                if (num > n * n) break;
            }
            check++;
            if (check == 2) {
                cnt++;
                check = 0;
            }
            d = d < 3 ? d + 1 : 0;
        }

        StringBuilder sb = new StringBuilder();
        int[] searchResult = new int[2];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == s) searchResult = new int[]{i + 1, j + 1};
                sb.append(board[i][j]).append(" ");
            }
            sb.append("\n");
        }
        sb.append(searchResult[0]).append(" ").append(searchResult[1]);
        System.out.println(sb);

    }
}
