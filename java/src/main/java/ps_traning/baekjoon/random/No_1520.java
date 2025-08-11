package ps_traning.baekjoon.random;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_1520 {

    private static int n, m;
    private static int[][] board;
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[][] visited = new int[n][m];
        for (int i = 0; i < n; i++) {
            Arrays.fill(visited[i], -1);
        }
        recursion(0, 0, visited);

        System.out.println(visited[0][0]);

    }

    private static int recursion(int y, int x, int[][] visited) {
        if (y == n - 1 && x == m - 1) {
            visited[y][x] = 1;
            return 1;
        }

        int result = 0;
        for (int d = 0; d < 4; d++) {
            int ny = y + dy[d];
            int nx = x + dx[d];
            if (ny >= n || nx >= m || ny < 0 || nx < 0 || board[y][x] <= board[ny][nx])
                continue;
            if (visited[ny][nx] != -1) {
                visited[y][x] += visited[ny][nx];
                continue;
            }
            visited[y][x] += recursion(ny, nx, visited);
        }
        visited[y][x] += 1;
        result = visited[y][x];
        return result;
    }
}
