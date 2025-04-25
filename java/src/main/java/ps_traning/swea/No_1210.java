package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_1210 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int[] dx = {-1, 1};

        for (int tc = 1; tc <= 10; tc++) {
            tc = Integer.valueOf(br.readLine());
            sb.append("#").append(tc).append(" ");

            int y = 99;
            int x = 0;
            int[][] board = new int[100][100];
            for (int i = 0; i < 100; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 100; j++) {
                    board[i][j] = Integer.valueOf(st.nextToken());
                    if (board[i][j] == 2) {
                        x = j;
                    }
                }
            }

            while (y > 0) {
                for (int d = 0; d < 2; d++) {
                    int nx = x + dx[d];
                    if (nx < 0 || nx > 99 || board[y][nx] == 0) continue;
                    while (nx >= 0 && nx < 100 && board[y][nx] == 1) {
                        x = nx;
                        nx = x + dx[d];
                    }
                    break;
                }
                y--;
            }

            sb.append(x).append("\n");
        }

        System.out.print(sb);
    }
}
