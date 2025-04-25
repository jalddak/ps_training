package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class No_2206 {
    private static int n, m;
    private static int[][] board;
    private static boolean[][][] visited;
    private static int[] dy, dx;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.valueOf(st.nextToken());
        m = Integer.valueOf(st.nextToken());

        board = new int[n][m];
        visited = new boolean[n][m][2];
        for (int i = 0; i < n; i++) {
            char[] temp = br.readLine().toCharArray();
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.valueOf(temp[j] - '0');
            }
        }

        dy = new int[]{-1, 0, 1, 0};
        dx = new int[]{0, 1, 0, -1};
        int answer = solution();
        System.out.println(answer);
    }

    private static int solution() {
        if (n == 1 && m == 1) return 1;
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{0, 0, 1, 0});
        visited[0][0] = new boolean[]{true, true};

        while (!q.isEmpty()) {
            int[] qr = q.poll();
            int y = qr[0], x = qr[1], cnt = qr[2], bn = qr[3];

            for (int d = 0; d < 4; d++) {
                int ny = y + dy[d];
                int nx = x + dx[d];
                if (ny >= n || ny < 0 || nx >= m || nx < 0 || visited[ny][nx][bn] || (bn == 1 && board[ny][nx] == 1))
                    continue;
                if (ny == n - 1 && nx == m - 1) {
                    return cnt + 1;
                }
                int nBn = bn;
                if (board[ny][nx] == 1) nBn = 1;
                visited[ny][nx][nBn] = true;
                q.add(new int[]{ny, nx, cnt + 1, nBn});
            }
        }

        return -1;
    }
}
