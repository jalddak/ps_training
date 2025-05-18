package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_1211 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = 10;
        for (int a = 0; a < tcCnt; a++) {
            int tc = Integer.valueOf(br.readLine());
            sb.append("#").append(tc).append(" ");

            int[][] board = new int[100][100];
            for (int i = 0; i < 100; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 100; j++) {
                    board[i][j] = Integer.valueOf(st.nextToken());
                }
            }

            int result = -1;
            int min_t = 10000;
            for (int i = 0; i < 100; i++) {
                if (board[0][i] == 0) continue;
                int candidate = check(board, i);
                if (candidate < min_t) {
                    min_t = candidate;
                    result = i;
                }
            }

            sb.append(result).append("\n");
        }
        System.out.print(sb);

    }

    private static int check(int[][] board, int start){
        int x = start;
        int y = 0;

        int result = 1;
        while (y < 100){
            if (x - 1 >= 0 && board[y][x - 1] == 1) {
                while (x - 1 >= 0 && board[y][x - 1] == 1){
                    x--;
                    result++;
                }
            } else if (x + 1 < 100 && board[y][x + 1] == 1) {
                while (x + 1 < 100 && board[y][x + 1] == 1){
                    x++;
                    result++;
                }
            }
            y++;
            result++;
        }


        return result;

    }
}
