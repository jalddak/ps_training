package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class No_7576 {

    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int[][] board = new int[n][m];
        int cnt = 0;

        Queue<int[]> q = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] == 0) cnt++;
                if (board[i][j] == 1) q.add(new int[]{i, j, 0});
            }
        }

        int result = 0;
        while (!q.isEmpty()) {
            int[] poll = q.poll();
            int y = poll[0], x = poll[1], t = poll[2];
            if (cnt == 0) break;

            for (int d = 0; d < 4; d++) {
                int ny = y + dy[d];
                int nx = x + dx[d];
                int nt = t + 1;
                if (ny >= n || nx >= m || ny < 0 || nx < 0 || board[ny][nx] != 0) continue;
                q.add(new int[]{ny, nx, nt});
                board[ny][nx] = 1;
                cnt--;
                if (cnt == 0) {
                    result = nt;
                    break;
                }
            }
        }

        if (cnt != 0) result = -1;

        System.out.println(result);
    }
}
