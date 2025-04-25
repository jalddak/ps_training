package ps_traning.solvedAC.class_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class No_9252_intBoard {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str1 = br.readLine();
        String str2 = br.readLine();

        int len1 = str1.length();
        int len2 = str2.length();

        int[][] board = new int[len1 + 1][len2 + 1];

        for (int i = 0; i < len1; i++) {
            for (int j = 0; j < len2; j++) {
                if (str1.charAt(i) == str2.charAt(j)) {
                    board[i + 1][j + 1] = board[i][j] + 1;
                } else {
                    board[i + 1][j + 1] = Math.max(board[i + 1][j], board[i][j + 1]);
                }
            }
        }

        System.out.println(board[len1][len2]);
        StringBuilder sb = new StringBuilder();
        int index1 = len1, index2 = len2;
        while (sb.length() < board[len1][len2]) {
            if (board[index1][index2] == board[index1 - 1][index2]) index1--;
            else if (board[index1][index2] == board[index1][index2 - 1]) index2--;
            else {
                sb.append(str1.charAt(index1 - 1));
                index1--;
                index2--;
            }
        }
        System.out.println(sb.reverse().toString());
    }
}
