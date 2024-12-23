package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class No_2178 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken());
        int m = Integer.valueOf(st.nextToken());
        int[][] board = new int[n][m];

        for (int i = 0; i < n; i++) {
            char[] input = br.readLine().toCharArray();
            for (int j = 0; j < m; j++) {
                board[i][j] = input[j] - '0';
            }
        }

        boolean[][] visited = new boolean[n][m];
        visited[0][0] = true;
        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, 1, 0, -1};
        Queue<int[]> q = new LinkedList<>(List.of(new int[]{0, 0, 1}));

        while (!q.isEmpty()) {
            int[] input = q.poll();
            int y = input[0], x = input[1], cnt = input[2];
            int nCnt = cnt + 1;
            for (int d = 0; d < 4; d++) {
                int ny = y + dy[d];
                int nx = x + dx[d];
                if (ny >= 0 && ny < n && nx >= 0 && nx < m && board[ny][nx] == 1 && !visited[ny][nx]) {
                    if (ny == n - 1 && nx == m - 1) {
                        System.out.println(nCnt);
                        System.exit(0);
                    }
                    visited[ny][nx] = true;
                    q.add(new int[]{ny, nx, nCnt});
                }
            }
        }
    }
}
