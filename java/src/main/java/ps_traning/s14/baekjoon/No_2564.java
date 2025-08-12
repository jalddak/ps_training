package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class No_2564 {

    private static int n, m;
    private static boolean[][] board;
    private static boolean[][] visited;
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        m = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(br.readLine());

        board = new boolean[n + 1][m + 1];
        visited = new boolean[n + 1][m + 1];

        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                if (i == 1 || i == n - 1) {
                    visited[i][j] = true;
                }
                if (j == 1 || j == m - 1) {
                    visited[i][j] = true;
                }
            }
        }

        int[] ty = {0, n, 1, 1};
        int[] tx = {1, 1, 0, m};
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken()) - 1;
            int y = ty[d];
            int x = tx[d];

            int p = Integer.parseInt(st.nextToken());
            if (d > 1) y *= p;
            else x *= p;

            board[y][x] = true;
        }


        st = new StringTokenizer(br.readLine());
        int d = Integer.parseInt(st.nextToken()) - 1;
        int y = ty[d];
        int x = tx[d];

        int p = Integer.parseInt(st.nextToken());
        if (d > 1) y *= p;
        else x *= p;
        visited[y][x] = true;

        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{y, x, 0});
        int result = 0;
        while (!q.isEmpty()) {
            int[] poll = q.poll();
            y = poll[0];
            x = poll[1];
            int cnt = poll[2];
            for (d = 0; d < 4; d++) {
                int ny = y + dy[d];
                int nx = x + dx[d];
                if (ny >= n + 1 || nx >= m + 1 || ny < 0 || nx < 0 || visited[ny][nx]) continue;
                visited[ny][nx] = true;
                if (board[ny][nx]) result += cnt + 1;
                q.offer(new int[]{ny, nx, cnt + 1});
            }
        }

        System.out.println(result);
    }
}