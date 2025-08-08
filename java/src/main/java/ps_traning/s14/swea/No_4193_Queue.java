package ps_traning.s14.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

class No_4193_Queue {

    private static int[] dy = {-1, 0, 1, 0, 0};
    private static int[] dx = {0, 1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int tcCnt = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int tc = 1; tc <= tcCnt; tc++) {
            int n = Integer.parseInt(br.readLine());

            StringTokenizer st = null;
            int[][] board = new int[n][n];
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    board[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            st = new StringTokenizer(br.readLine());
            int sy = Integer.parseInt(st.nextToken());
            int sx = Integer.parseInt(st.nextToken());
            st = new StringTokenizer(br.readLine());
            int ey = Integer.parseInt(st.nextToken());
            int ex = Integer.parseInt(st.nextToken());

            Queue<int[]> q = new ArrayDeque<>();
            q.offer(new int[]{sy, sx, 0});
            boolean[][][] visited = new boolean[n][n][3];
//            visited[sy][sx][0] = true;

            int answer = -1;
            while (!q.isEmpty()) {
                int[] poll = q.poll();
                int y = poll[0], x = poll[1], t = poll[2];
                if (y == ey && x == ex) {
                    answer = t;
                    break;
                }
                for (int d = 0; d < 5; d++) {
                    int ny = y + dy[d];
                    int nx = x + dx[d];
                    if (ny >= n || nx >= n || ny < 0 || nx < 0 || board[ny][nx] == 1 || visited[ny][nx][t % 3]
                            || (d != 4 && board[ny][nx] == 2 && t % 3 != 2))
                        continue;
                    visited[ny][nx][t % 3] = true;
                    q.offer(new int[]{ny, nx, t + 1});
                }
            }
            sb.append("#").append(tc).append(" ").append(answer).append("\n");
        }
        System.out.print(sb);
    }
}

