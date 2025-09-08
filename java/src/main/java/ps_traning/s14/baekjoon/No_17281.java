package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_17281 {

    private static int n, answer;
    private static int[][] innings;
    private static int[] priority = new int[9];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        innings = new int[n][9];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 9; j++) innings[i][j] = Integer.parseInt(st.nextToken());
        }

        boolean[] visited = new boolean[9];
        visited[0] = true;
        recursion(0, visited);
        System.out.println(answer);

    }

    private static int calc() {
        int result = 0;
        int idx = 0;
        for (int i = 0; i < n; i++) {
            int out = 0;
            int[] board = new int[3];
            while (true) {
                if (out == 3) {
                    break;
                }
                int k = priority[idx];
                if (innings[i][k] == 0) {
                    out++;
                } else if (innings[i][k] == 1) {
                    result += board[2];
                    board[2] = board[1];
                    board[1] = board[0];
                    board[0] = 1;

                } else if (innings[i][k] == 2) {
                    result += (board[2] + board[1]);
                    board[2] = board[0];
                    board[1] = 1;
                    board[0] = 0;
                } else if (innings[i][k] == 3) {
                    result += (board[2] + board[1] + board[0]);
                    board[2] = 1;
                    board[1] = 0;
                    board[0] = 0;
                } else if (innings[i][k] == 4) {
                    result += board[2] + board[1] + board[0] + 1;
                    Arrays.fill(board, 0);
                }
                idx++;
                if (idx >= 9) idx -= 9;
            }
        }

        return result;
    }

    private static void recursion(int depth, boolean[] visited) {
        if (depth == 9) {
            answer = Math.max(answer, calc());
            return;
        }
        int nDepth = depth + 1;
        if (nDepth == 3) nDepth++;
        for (int i = 1; i < 9; i++) {
            if (visited[i]) continue;
            visited[i] = true;
            priority[depth] = i;
            recursion(nDepth, visited);
            visited[i] = false;
        }
    }
}
