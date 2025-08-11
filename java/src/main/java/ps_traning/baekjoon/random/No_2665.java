package ps_traning.baekjoon.random;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class No_2665 {

    private static int n;
    private static int[][] board;
    private static boolean[][] visited;
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        board = new int[n][n];
        visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            for (int j = 0; j < n; j++) {
                board[i][j] = s.charAt(j) - '0';
            }
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[2] - b[2]);
        pq.add(new int[]{0, 0, 0});
        visited[0][0] = true;

        int result = 0;
        while (!pq.isEmpty()) {
            int[] poll = pq.poll();
            int y = poll[0], x = poll[1], cnt = poll[2];
            if (y == n - 1 && x == n - 1) {
                result = cnt;
                break;
            }

            for (int d = 0; d < 4; d++) {
                int ny = y + dy[d];
                int nx = x + dx[d];
                if (ny >= n || nx >= n || ny < 0 || nx < 0 || visited[ny][nx]) continue;
                int nCnt = cnt;
                if (board[ny][nx] == 0) nCnt++;
                visited[ny][nx] = true;
                pq.offer(new int[]{ny, nx, nCnt});
            }
        }

        System.out.println(result);


    }
}
