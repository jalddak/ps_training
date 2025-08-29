package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

public class No_11559 {

    private static char[][] board = new char[12][6];
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 12; i++) {
            String input = br.readLine();
            for (int j = 0; j < 6; j++) {
                board[i][j] = input.charAt(j);
            }
        }

        int answer = 0;
        while (bfs()) {
            answer++;
            fall();
        }
        System.out.println(answer);
    }

    private static void fall() {
        for (int i = 0; i < 6; i++) {
            Queue<Integer> q = new ArrayDeque<>();
            for (int j = 11; j >= 0; j--) {
                if (board[j][i] == '.') {
                    q.add(j);
                    continue;
                }
                if (q.isEmpty()) continue;
                board[q.poll()][i] = board[j][i];
                board[j][i] = '.';
                q.add(j);
            }

        }
    }

    private static boolean bfs() {
        boolean result = false;
        boolean[][] visited = new boolean[12][6];
        for (int i = 11; i >= 0; i--) {
            for (int j = 5; j >= 0; j--) {
                if (board[i][j] == '.' || visited[i][j]) continue;
                Queue<int[]> q = new ArrayDeque<>();
                visited[i][j] = true;
                q.add(new int[]{i, j});
                char color = board[i][j];
                int cnt = 1;
                Queue<int[]> save = new ArrayDeque<>();
                while (!q.isEmpty()) {
                    int[] poll = q.poll();
                    save.add(poll);
                    int y = poll[0], x = poll[1];
                    for (int d = 0; d < 4; d++) {
                        int ny = y + dy[d];
                        int nx = x + dx[d];
                        if (ny >= 12 || nx >= 6 || ny < 0 || nx < 0 || board[ny][nx] != color || visited[ny][nx])
                            continue;
                        visited[ny][nx] = true;
                        q.add(new int[]{ny, nx});
                        cnt++;
                    }
                }

                if (cnt < 4) continue;
                result = true;
                while (!save.isEmpty()) {
                    int[] poll = save.poll();
                    int y = poll[0], x = poll[1];
                    board[y][x] = '.';
                }
            }
        }
        return result;
    }
}