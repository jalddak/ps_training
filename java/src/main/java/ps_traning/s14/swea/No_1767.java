package ps_traning.s14.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

class No_1767 {

    private static int n, k, linked, answer;
    private static int[][] board;
    private static List<int[]> cores;
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};
    private static boolean[] flags;
    private static int[] lengths;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tcCnt = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int tc = 1; tc <= tcCnt; tc++) {
            n = Integer.parseInt(br.readLine());
            board = new int[n][n];
            cores = new ArrayList<>();
            linked = 0;
            answer = Integer.MAX_VALUE;
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    board[i][j] = Integer.parseInt(st.nextToken());
                    if (i == n - 1 || j == n - 1 || i == 0 || j == 0 || board[i][j] == 0) continue;
                    cores.add(new int[]{i, j});
                }
            }

            k = cores.size();
            flags = new boolean[k];
            lengths = new int[k];

            recursion(0);
            sb.append("#").append(tc).append(" ").append(answer).append("\n");
        }
        System.out.println(sb);
    }

    private static void recursion(int depth) {
        if (depth == k) {
            int cnt = 0;
            int len = 0;
            for (int i = 0; i < k; i++) {
                if (!flags[i]) continue;
                cnt++;
                len += lengths[i];
            }
            if (cnt >= linked) {
                if (linked < cnt) {
                    linked = cnt;
                    answer = Integer.MAX_VALUE;
                }
                answer = Math.min(answer, len);
            }
            return;
        }

        boolean zeroLink = false;
        int y = cores.get(depth)[0];
        int x = cores.get(depth)[1];
        for (int d = 0; d < 4; d++) {
            draw(y, x, d, depth);
            if (zeroLink && !flags[depth]) continue;
            if (!flags[depth]) zeroLink = true;
            recursion(depth + 1);
            if (flags[depth]) remove(y, x, d, depth);
        }
    }

    private static void draw(int y, int x, int d, int idx) {
        flags[idx] = true;
        lengths[idx] = 0;
        int ny = y + dy[d];
        int nx = x + dx[d];
        while (true) {
            if (ny >= n || nx >= n || ny < 0 || nx < 0) break;
            if (board[ny][nx] != 0) {
                flags[idx] = false;
                break;
            }
            board[ny][nx] = 2;
            ny += dy[d];
            nx += dx[d];
            lengths[idx]++;
        }

        if (!flags[idx]) remove(y, x, d, idx);
    }

    private static void remove(int y, int x, int d, int idx) {
        int ny = y;
        int nx = x;
        for (int i = 0; i < lengths[idx]; i++) {
            ny += dy[d];
            nx += dx[d];
            board[ny][nx] = 0;
        }
    }
}
