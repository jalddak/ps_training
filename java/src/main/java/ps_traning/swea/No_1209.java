package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_1209 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        for (int tc = 1; tc <= 10; tc++) {
            tc = Integer.valueOf(br.readLine());
            sb.append("#").append(tc).append(" ");

            int[][] board = new int[100][100];
            for (int i = 0; i < 100; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < 100; j++) {
                    board[i][j] = Integer.valueOf(st.nextToken());
                }
            }

            int result = 0;
            int diagSum = 0;
            int antiDiagSum = 0;
            for (int i = 0; i < 100; i++) {
                int rowSum = 0;
                int colSum = 0;
                for (int j = 0; j < 100; j++) {
                    rowSum += board[i][j];
                    colSum += board[j][i];
                    if (i == j) diagSum += board[i][j];
                    if (i + j == 99) antiDiagSum += board[i][j];
                }
                result = Math.max(result, Math.max(rowSum, colSum));
            }
            result = Math.max(result, Math.max(antiDiagSum, diagSum));
            sb.append(result).append("\n");
        }
        System.out.print(sb);
    }
}
