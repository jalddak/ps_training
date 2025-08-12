package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class No_2567 {

    private static int n;
    private static int[][] board = new int[101][101];
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int y = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            draw(y, x);
        }

        boolean[][] visited = new boolean[101][101];
        int result = 0;
        for (int i = 0; i < 101; i++) {
            for (int j = 0; j < 101; j++) {
                if (board[i][j] == 0 || visited[i][j]) continue;
                visited[i][j] = true;
                Queue<int[]> q = new ArrayDeque<>();
                q.offer(new int[]{i, j});
                while (!q.isEmpty()) {
                    int[] poll = q.poll();
                    int y = poll[0], x = poll[1];
                    for (int d = 0; d < 4; d++) {
                        int ny = y + dy[d];
                        int nx = x + dx[d];
                        if (ny >= 101 || nx >= 101 || ny < 0 || nx < 0 || board[ny][nx] == 0) {
                            result += 1;
                            continue;
                        }
                        if (visited[ny][nx]) continue;
                        visited[ny][nx] = true;
                        q.offer(new int[]{ny, nx});
                    }
                }
            }
        }

        System.out.println(result);
    }

    private static void draw(int y, int x) {
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                board[y + i][x + j] = 1;
            }
        }
    }
}
