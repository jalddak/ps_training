import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    private static int n, m;
    private static int[][] board;
    private static boolean[][][] visited;
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.valueOf(st.nextToken());
        m = Integer.valueOf(st.nextToken());

        board = new int[n][m];
        visited = new boolean[n][m][2];

        for (int i = 0; i < n; i++) {
            board[i] = br.readLine().chars().map(c -> c - '0').toArray();
        }

        visited[0][0][0] = true;
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0, 0, 1});

        int answer = -1;
        while (!queue.isEmpty()) {
            int[] poll = queue.poll();
            int y = poll[0], x = poll[1], b = poll[2], cnt = poll[3];

            if (y == n - 1 && x == m - 1) {
                answer = cnt;
                break;
            }

            for (int d = 0; d < 4; d++) {
                int ny = y + dy[d];
                int nx = x + dx[d];
                if (ny >= n || ny < 0 || nx >= m || nx < 0 || visited[ny][nx][0]) continue;
                if (board[ny][nx] == 1 && b == 1) continue;
                int nb = b;
                if (board[ny][nx] == 1) nb += 1;
                if (visited[ny][nx][nb]) continue;
                visited[ny][nx][nb] = true;
                queue.offer(new int[]{ny, nx, nb, cnt + 1});
            }
        }

        System.out.println(answer);
    }
}