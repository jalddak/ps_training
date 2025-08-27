package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class No_4485 {

    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringBuilder sb = new StringBuilder();
        int pNum = 1;
        while (true) {
            int n = Integer.parseInt(br.readLine());
            if (n == 0) break;
            int[][] board = new int[n][n];
            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    board[i][j] = Integer.parseInt(st.nextToken());
                }
            }

            boolean[][] visited = new boolean[n][n];
            PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
                return a[0] - b[0];
            });

            visited[0][0] = true;
            int result = board[0][0];
            pq.offer(new int[]{result, 0, 0});
            while (!pq.isEmpty()) {
                int[] poll = pq.poll();
                int r = poll[0], y = poll[1], x = poll[2];
                if (y == n - 1 && x == n - 1) {
                    result = r;
                    break;
                }
                for (int d = 0; d < 4; d++) {
                    int ny = y + dy[d];
                    int nx = x + dx[d];
                    if (ny >= n || nx >= n || ny < 0 || nx < 0 || visited[ny][nx]) continue;
                    visited[ny][nx] = true;
                    pq.offer(new int[]{r + board[ny][nx], ny, nx});
                }
            }
            sb.append("Problem ").append(pNum++).append(": ").append(result).append("\n");
        }
        System.out.print(sb);
    }
}
