package ps_traning.swea;


import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class No_4193 {

    private static StringBuilder sb = new StringBuilder();
    private static int n, sy, sx, ey, ex;
    private static int[][] board;
    private static boolean[][] visited;
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= t; tc++) {
            n = Integer.valueOf(br.readLine());
            board = new int[n][n];
            visited = new boolean[n][n];
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) board[i][j] = Integer.valueOf(st.nextToken());
            }
            StringTokenizer st = new StringTokenizer(br.readLine());
            sy = Integer.valueOf(st.nextToken());
            sx = Integer.valueOf(st.nextToken());
            st = new StringTokenizer(br.readLine());
            ey = Integer.valueOf(st.nextToken());
            ex = Integer.valueOf(st.nextToken());
            int answer = bfs();
            sb.append("#").append(tc).append(" ").append(answer).append("\n");
        }
        System.out.print(sb);
    }

    private static int bfs() {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{sy, sx, 0});
        visited[sy][sx] = true;

        int result = -1;
        while (!q.isEmpty()) {
            int[] poll = q.poll();
            int y = poll[0], x = poll[1], time = poll[2];
            if (y == ey && x == ex) {
                result = time;
                break;
            }
            for (int d = 0; d < 4; d++) {
                int ny = y + dy[d];
                int nx = x + dx[d];
                if (ny < 0 || nx < 0 || ny >= n || nx >= n || board[ny][nx] == 1 || visited[ny][nx]) continue;
                if (time % 3 != 2 && board[ny][nx] == 2) {
                    ny = y;
                    nx = x;
                }
                visited[ny][nx] = true;
                q.offer(new int[]{ny, nx, time + 1});
            }
        }
        return result;
    }

}