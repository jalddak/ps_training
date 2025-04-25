package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class No_2805 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("#").append(tc).append(" ");

            int n = Integer.valueOf(br.readLine());
            int[][] board = new int[n][n];

            for (int i = 0; i < n; i++) {
                int[] row = br.readLine().chars().map(c -> c - '0').toArray();
                board[i] = row;
            }

            int mid = n / 2;

            int result = 0;
            for (int i = 0; i < n; i++) {
                int range = mid - Math.abs(i - mid);
                result += Arrays.stream(Arrays.copyOfRange(board[i], mid - range, mid + 1 + range)).sum();
            }
            sb.append(result).append("\n");
        }

        System.out.print(sb);
    }
}
