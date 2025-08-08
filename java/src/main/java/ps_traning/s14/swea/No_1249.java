package ps_traning.s14.swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

class No_1249 {

    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tcCnt = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int tc = 1; tc <= tcCnt; tc++) {
            int n = Integer.parseInt(br.readLine());
            int[][] board = new int[n][n];
            boolean[][] visited = new boolean[n][n];
            for (int i = 0; i < n; i++) {
                String s = br.readLine();
                for (int j = 0; j < n; j++) board[i][j] = s.charAt(j) - '0';
            }

            visited[0][0] = true;
            PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[2] - b[2]);
            pq.offer(new int[]{0, 0, 0});
            int answer = -1;
            while (!pq.isEmpty()) {
                int[] poll = pq.poll();
                int y = poll[0], x = poll[1], t = poll[2];
                if (y == n - 1 && x == n - 1) {
                    answer = t;
                    break;
                }
                for (int d = 0; d < 4; d++) {
                    int ny = y + dy[d];
                    int nx = x + dx[d];
                    if (ny >= n || nx >= n || ny < 0 || nx < 0 || visited[ny][nx]) continue;
                    visited[ny][nx] = true;
                    pq.offer(new int[]{ny, nx, t + board[ny][nx]});
                }
            }

            sb.append("#").append(tc).append(" ").append(answer).append("\n");
        }
        System.out.print(sb);
    }
}
