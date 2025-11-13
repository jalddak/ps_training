import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

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
            String row = br.readLine();
            for (int j = 0; j < m; j++) board[i][j] = row.charAt(j) - '0';
        }

        boolean[][][] visited = new boolean[n][m][2];

        visited[0][0][0] = true;
        Queue<int[]> q = new ArrayDeque<>();
        q.add(new int[]{1, 0, 0, 0});

        int result = -1;
        while (!q.isEmpty()) {
            // cnt, y, x, bk
            int[] poll = q.poll();
            int cnt = poll[0], y = poll[1], x = poll[2], bk = poll[3];
            if (y == n - 1 && x == m - 1) {
                result = cnt;
                break;
            }
            for (int d = 0; d < 4; d++) {
                int ny = y + dy[d];
                int nx = x + dx[d];
                if (ny >= n || nx >= m || ny < 0 || nx < 0 || visited[ny][nx][0]) continue;
                int nBk = bk;
                if (board[ny][nx] == 1) {
                    if (bk == 1) continue;
                    else nBk = 1;
                }
                if (visited[ny][nx][nBk]) continue;
                visited[ny][nx][nBk] = true;
                q.add(new int[]{cnt + 1, ny, nx, nBk});
            }
        }
        System.out.println(result);
    }
}