package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class No_14502 {

    private static int n, m;
    private static int[][] board;
    private static List<int[]> blanks = new ArrayList<>();
    private static int answer = 0;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        board = new int[n][m];

        blanks = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] == 0) blanks.add(new int[]{i, j});
            }
        }

        makeWalls(0, 0);
        System.out.println(answer);
    }

    private static void makeWalls(int depth, int start) {
        if (depth == 3) {
            spread();
            return;
        }

        for (int i = start; i < blanks.size(); i++) {
            int y = blanks.get(i)[0];
            int x = blanks.get(i)[1];
            board[y][x] = 1;
            makeWalls(depth + 1, i + 1);
            board[y][x] = 0;
        }
    }

    private static void spread() {
        boolean[][] visited = new boolean[n][m];
        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, 1, 0, -1};
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (visited[i][j] || board[i][j] != 2) continue;
                visited[i][j] = true;
                Queue<int[]> q = new ArrayDeque<>();
                q.add(new int[]{i, j});
                while (!q.isEmpty()) {
                    int[] poll = q.poll();
                    int y = poll[0], x = poll[1];
                    for (int d = 0; d < 4; d++) {
                        int ny = y + dy[d];
                        int nx = x + dx[d];
                        if (ny >= n || nx >= m || ny < 0 || nx < 0 || board[ny][nx] == 1 || visited[ny][nx]) continue;
                        visited[ny][nx] = true;
                        q.add(new int[]{ny, nx});
                    }
                }
            }
        }
        int cnt = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 0 && !visited[i][j]) cnt++;
            }
        }
        answer = Math.max(answer, cnt);
    }
}
