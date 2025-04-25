package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class No_1249 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tcCnt = Integer.valueOf(br.readLine());

        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, 1, 0, -1};

        StringBuilder sb = new StringBuilder();
        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("#").append(tc).append(" ");
            int n = Integer.valueOf(br.readLine());
            int[][] board = new int[n][n];
            for (int i = 0; i < n; i++) {
                board[i] = br.readLine().chars().map(c -> c - '0').toArray();
            }

            PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
            pq.add(new int[]{0, 0, 0});
            boolean[][] visited = new boolean[n][n];

            while (!pq.isEmpty()) {
                int[] cur = pq.poll();
                int cnt = cur[0], y = cur[1], x = cur[2];
                if (y == n - 1 && x == n - 1) {
                    sb.append(cnt).append("\n");
                    break;
                }
                if (visited[y][x]) continue;
                visited[y][x] = true;
                for (int d = 0; d < 4; d++) {
                    int ny = y + dy[d];
                    int nx = x + dx[d];
                    if (nx < 0 || ny < 0 || nx >= n || ny >= n || visited[ny][nx]) continue;
                    pq.add(new int[]{cnt + board[ny][nx], ny, nx});
                }
            }
        }
        System.out.print(sb.toString());
    }
}
