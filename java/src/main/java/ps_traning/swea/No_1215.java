package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_1215 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        for (int tc = 1; tc <= 10; tc++) {
            sb.append("#").append(tc).append(" ");
            int n = Integer.valueOf(br.readLine());

            char[][] board = new char[8][8];
            for (int i = 0; i < 8; i++) board[i] = br.readLine().toCharArray();

            int result = 0;
            for (int i = 0; i < 8; i++) {
                for (int j = n - 1; j < 8; j++) {
                    int l = j - (n - 1);
                    int r = j;

                    boolean rowCheck = true;
                    boolean colCheck = true;
                    result += 2;
                    while (l <= r && (rowCheck || colCheck)) {
                        if (rowCheck && board[i][l] != board[i][r]) {
                            result -= 1;
                            rowCheck = false;
                        }
                        if (colCheck && board[l][i] != board[r][i]) {
                            result -= 1;
                            colCheck = false;
                        }
                        l++;
                        r--;
                    }
                }
            }

            sb.append(result).append("\n");
        }
        System.out.print(sb);
    }
}
