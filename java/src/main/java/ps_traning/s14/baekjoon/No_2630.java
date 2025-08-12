package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class No_2630 {

    private static int n;
    private static int[][] board;
    private static int[] answer = new int[2];
    private static int[] dy = {0, 0, 1, 1};
    private static int[] dx = {0, 1, 0, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        board = new int[n][n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        recursion(n, 0, 0);
        System.out.println(answer[0]);
        System.out.println(answer[1]);
    }

    private static int recursion(int length, int y, int x) {
        if (length == 1) {
            answer[board[y][x]] += 1;
            return board[y][x];
        }

        Set<Integer> set = new HashSet<>();
        for (int d = 0; d < 4; d++) {
            int nl = length / 2;
            int ny = y + dy[d] * nl;
            int nx = x + dx[d] * nl;
            set.add(recursion(nl, ny, nx));
        }

        if (set.contains(2) || set.size() > 1) return 2;

        int result = -1;
        for (int n : set) {
            answer[n] -= 3;
            result = n;
        }
        return result;
    }
}