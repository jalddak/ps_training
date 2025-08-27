package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_1194 {

    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        char[][] board = new char[n][m];
        int sy = -1;
        int sx = -1;
        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            for (int j = 0; j < m; j++) {
                board[i][j] = input.charAt(j);
                if (board[i][j] == '0') {
                    sy = i;
                    sx = j;
                }
            }
        }

        boolean[][][] visited = new boolean[64][n][m];
        visited[0][sy][sx] = true;
        Queue<int[]> q = new ArrayDeque<>();
        q.offer(new int[]{0, sy, sx, 0});

        Set<Character> lower = new HashSet<>();
        Set<Character> upper = new HashSet<>();
        for (int i = 0; i < 6; i++) {
            lower.add((char) (i + 'a'));
            upper.add((char) (i + 'A'));
        }

        int result = -1;
        while (!q.isEmpty()) {
            int[] poll = q.poll();
            int k = poll[0], y = poll[1], x = poll[2], cnt = poll[3];
            if (board[y][x] == '1') {
                result = poll[3];
                break;
            }
            for (int d = 0; d < 4; d++) {
                int ny = y + dy[d];
                int nx = x + dx[d];
                int nk = k;
                int nCnt = cnt + 1;
                if (ny >= n || nx >= m || ny < 0 || nx < 0 || board[ny][nx] == '#' || visited[nk][ny][nx]) continue;
                if (upper.contains(board[ny][nx])) {
                    int key = 1 << (board[ny][nx] - 'A');
                    if ((key & k) != key) continue;
                }
                if (lower.contains(board[ny][nx])) {
                    int key = 1 << (board[ny][nx] - 'a');
                    nk = nk | key;
                }
                visited[nk][ny][nx] = true;
                q.offer(new int[]{nk, ny, nx, nCnt});
            }
        }
        System.out.println(result);
    }
}