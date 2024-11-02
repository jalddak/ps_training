package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_1018 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] nm = new int[2];
        int i = 0;
        while (st.hasMoreTokens()) nm[i++] = Integer.valueOf(st.nextToken());
        int n = nm[0];
        int m = nm[1];
        char[][] board = new char[n][m];
        for (i = 0; i < n; i++) {
            int j = 0;
            for (char c : br.readLine().toCharArray()) {
                board[i][j++] = c;
            }
        }

        char[][] chess = new char[8][8];
        int answer = n * m;
        for (i = 0; i <= n - 8; i++) {
            for (int j = 0; j <= m - 8; j++) {
                for (int a = 0; a < 8; a++) {
                    for (int b = 0; b < 8; b++) {
                        chess[a][b] = board[i + a][j + b];
                    }
                }
                answer = Math.min(answer, minCheck(chess));
            }
        }
        System.out.println(answer);
    }

    public static int minCheck(char[][] board) {
        int cnt = 0;
        for (int i = 1; i < 8; i++) {
            char temp = board[i - 1][0] == 'B' ? 'W' : 'B';
            if (temp != board[i][0]) {
                board[i][0] = temp;
                cnt++;
            }
        }
        for (int i = 0; i < 8; i++) {
            for (int j = 1; j < 8; j++) {
                char temp = board[i][j - 1] == 'B' ? 'W' : 'B';
                if (temp != board[i][j]) {
                    board[i][j] = temp;
                    cnt++;
                }
            }
        }
        cnt = Math.min(cnt, 64 - cnt);
        return cnt;
    }
}
