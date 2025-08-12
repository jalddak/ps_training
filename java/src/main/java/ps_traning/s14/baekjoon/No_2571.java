package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_2571 {

    private static int n, result;
    private static int[][] board = new int[101][101];

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int y = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            draw(y, x);
        }

        int[][] lengths = new int[101][101];
        for (int i = 0; i < 101; i++) {
            for (int j = 0; j < 101; j++) {
                if (board[j][i] != 0) {
                    int beforeC = j > 0 ? lengths[j - 1][i] : 0;
                    lengths[j][i] = beforeC + 1;
                }
            }
        }

        checkMax(lengths);
        System.out.println(result);
    }

    private static void draw(int y, int x) {
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                board[y + i][x + j] = 1;
            }
        }
    }

    private static void checkMax(int[][] lengths) {
        for (int i = 0; i < 101; i++) {
            for (int j = 0; j < 101; j++) {
                if (lengths[i][j] == 0) continue;
                int cnt = 0;
                int minH = 1000;
                for (int k = j; k < 101; k++) {
                    if (lengths[i][k] == 0) break;
                    cnt++;
                    minH = Math.min(minH, lengths[i][k]);
                    result = Math.max(result, minH * cnt);
                }
            }
        }
    }
}

