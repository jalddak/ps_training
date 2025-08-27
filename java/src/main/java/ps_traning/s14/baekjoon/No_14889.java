package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_14889 {

    private static int n, answer;
    private static int[][] board;
    private static boolean[] check;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        board = new int[n][n];
        check = new boolean[n];
        answer = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        recursion(0, 0);
        System.out.println(answer);
    }

    private static void recursion(int depth, int idx) {
        if (depth == n / 2) {
            calcSynergy();
            return;
        }

        for (int i = idx; i < n; i++) {
            check[i] = true;
            recursion(depth + 1, i + 1);
            check[i] = false;
        }
    }

    private static void calcSynergy() {
        int[] ts = new int[n / 2];
        int[] fs = new int[n / 2];

        int ti = 0;
        int fi = 0;
        for (int i = 0; i < n; i++) {
            if (check[i]) ts[ti++] = i;
            if (!check[i]) fs[fi++] = i;
        }

        int tSum = 0;
        int fSum = 0;
        for (int i = 0; i < n / 2 - 1; i++) {
            for (int j = i + 1; j < n / 2; j++) {
                tSum += board[ts[i]][ts[j]] + board[ts[j]][ts[i]];
                fSum += board[fs[i]][fs[j]] + board[fs[j]][fs[i]];
            }
        }

        answer = Math.min(answer, Math.abs(tSum - fSum));
    }
}
