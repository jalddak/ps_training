package ps_traning.barkingdog.x09;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_11967 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken());
        int m = Integer.valueOf(st.nextToken());

        boolean[][] board = new boolean[n][n];
        boolean[][] visited = new boolean[n][n];
        List<int[]>[][] switchs = new List[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                switchs[i][j] = new ArrayList<>();
            }
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.valueOf(st.nextToken()) - 1;
            int y = Integer.valueOf(st.nextToken()) - 1;
            int a = Integer.valueOf(st.nextToken()) - 1;
            int b = Integer.valueOf(st.nextToken()) - 1;

            switchs[x][y].add(new int[]{a, b});
        }

        board[0][0] = true;
        visited[0][0] = true;
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{0, 0});

        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, 1, 0, -1};

        while (!q.isEmpty()) {
            int[] poll = q.poll();
            int x = poll[0], y = poll[1];
            for (int[] crd : switchs[x][y]) {
                int sx = crd[0], sy = crd[1];
                if (!board[sx][sy] && visited[sx][sy]) q.offer(new int[]{sx, sy});
                board[sx][sy] = true;
            }
            for (int d = 0; d < 4; d++) {
                int nx = x + dx[d];
                int ny = y + dy[d];
                if (nx >= n || nx < 0 || ny >= n || ny < 0 || visited[nx][ny]) continue;
                if (board[nx][ny]) q.offer(new int[]{nx, ny});
                visited[nx][ny] = true;
            }
        }

        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j]) result++;
            }
        }
        System.out.println(result);
    }
}
