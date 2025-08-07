package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class No_1600 {

    private static int k, w, h;
    private static int[][] board;
    private static int[][] visited;
    private static int[] hy = {-1, -2, -2, -1, 1, 2, 2, 1};
    private static int[] hx = {-2, -1, 1, 2, 2, 1, -1, -2};
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        k = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        w = Integer.parseInt(st.nextToken());
        h = Integer.parseInt(st.nextToken());

        board = new int[h][w];
        visited = new int[h][w];

        for (int i = 0; i < h; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < w; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                visited[i][j] = -1;
            }
        }

        visited[0][0] = k;
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{0, 0, k, 0});
        int result = -1;
        while (!q.isEmpty()) {
            int[] poll = q.poll();
            int y = poll[0], x = poll[1], p = poll[2], cnt = poll[3];
            if (y == h - 1 && x == w - 1) {
                result = cnt;
                break;
            }
            for (int d = 0; d < 4; d++) {
                int ny = y + dy[d];
                int nx = x + dx[d];
                if (ny >= h || nx >= w || ny < 0 || nx < 0 || visited[ny][nx] >= p || board[ny][nx] == 1) continue;
                visited[ny][nx] = p;
                q.offer(new int[]{ny, nx, p, cnt + 1});
            }

            if (p == 0) continue;
            for (int d = 0; d < 8; d++) {
                int ny = y + hy[d];
                int nx = x + hx[d];
                if (ny >= h || nx >= w || ny < 0 || nx < 0 || visited[ny][nx] >= p - 1 || board[ny][nx] == 1) continue;
                visited[ny][nx] = p - 1;
                q.offer(new int[]{ny, nx, p - 1, cnt + 1});
            }
        }

        System.out.println(result);
    }
}