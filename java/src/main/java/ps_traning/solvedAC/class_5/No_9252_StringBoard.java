package ps_traning.solvedAC.class_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * 메모리 초과
 */

public class No_9252_StringBoard {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str1 = br.readLine();
        String str2 = br.readLine();

        int len1 = str1.length();
        int len2 = str2.length();

        String[][] board = new String[len1 + 1][len2 + 1];

        for (int i = 0; i <= len1; i++) {
            for (int j = 0; j <= len2; j++) {
                board[i][j] = "";
            }
        }

        for (int i = 0; i < len1; i++) {
            for (int j = 0; j < len2; j++) {
                if (str1.charAt(i) == str2.charAt(j)) {
                    board[i + 1][j + 1] = board[i][j] + str1.charAt(i);
                } else {
                    board[i + 1][j + 1] = board[i + 1][j].length() > board[i][j + 1].length() ? board[i + 1][j] : board[i][j + 1];
                }
            }
        }

        System.out.println(board[len1][len2].length());
        System.out.println(board[len1][len2]);
    }
}
