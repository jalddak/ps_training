package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class No_7569 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());

        int[][][] board = new int[h][n][m];

        Queue<int[]> q = new ArrayDeque<>();
        int[] dz = {0, 0, 0, 0, 1, -1};
        int[] dy = {-1, 0, 1, 0, 0, 0};
        int[] dx = {0, 1, 0, -1, 0, 0};

        boolean[][][] visited = new boolean[h][n][m];
        int cnt = 0, all = 0;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < n; j++) {
                st = new StringTokenizer(br.readLine());
                for (int k = 0; k < m; k++) {
                    board[i][j][k] = Integer.parseInt(st.nextToken());
                    if (board[i][j][k] == 1) {
                        visited[i][j][k] = true;
                        q.add(new int[]{i, j, k});
                        cnt++;
                    }
                    if (board[i][j][k] != -1) all++;
                }
            }
        }

        int day = 0;

        while (!q.isEmpty() && cnt < all) {
            day++;
            Queue<int[]> next = new ArrayDeque<>();
            while (!q.isEmpty()) {
                int[] poll = q.poll();
                int z = poll[0], y = poll[1], x = poll[2];
                for (int d = 0; d < 6; d++) {
                    int nz = z + dz[d];
                    int ny = y + dy[d];
                    int nx = x + dx[d];
                    if (nz >= h || ny >= n || nx >= m || nz < 0 || ny < 0 || nx < 0 || board[nz][ny][nx] == -1 || visited[nz][ny][nx])
                        continue;
                    visited[nz][ny][nx] = true;
                    next.add(new int[]{nz, ny, nx});
                    cnt++;

                }
            }
            q = next;
        }

        System.out.println(cnt == all ? day : -1);
    }
}
