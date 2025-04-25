package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_9251 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str1 = br.readLine();
        String str2 = br.readLine();

        int len1 = str1.length();
        int len2 = str2.length();

        int[][] board = new int[len1][len2];

        for (int i = 0; i < len1; i++) {
            if (str1.charAt(i) == str2.charAt(0)) {
                for (int j = i; j < len1; j++) {
                    board[j][0] = 1;
                }
            }
        }

        for (int i = 0; i < len2; i++) {
            if (str2.charAt(i) == str1.charAt(0)) {
                for (int j = i; j < len2; j++) {
                    board[0][j] = 1;
                }
            }
        }

        for (int i = 1; i < len1; i++) {
            for (int j = 1; j < len2; j++) {
                if (str1.charAt(i) == str2.charAt(j)) {
                    board[i][j] = board[i - 1][j - 1] + 1;
                } else {
                    board[i][j] = Math.max(board[i - 1][j], board[i][j - 1]);
                }
            }
        }

        System.out.println(board[len1 - 1][len2 - 1]);
    }
}
