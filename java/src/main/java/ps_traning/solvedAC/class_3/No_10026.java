package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class No_10026 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());

        char[][] board = new char[n][n];
        for (int i = 0; i < n; i++) {
            board[i] = br.readLine().toCharArray();
        }

        Queue<int[]> q = new LinkedList<>();
        int normal = 0;
        int strange = 0;
        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, 1, 0, -1};

        boolean[][] visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    visited[i][j] = true;
                    normal += 1;
                    q.add(new int[]{i, j});
                    while (!q.isEmpty()) {
                        int[] r = q.poll();
                        int y = r[0], x = r[1];
                        for (int d = 0; d < 4; d++) {
                            int ny = y + dy[d];
                            int nx = x + dx[d];
                            if (ny >= 0 && ny < n && nx >= 0 && nx < n && !visited[ny][nx] && board[y][x] == board[ny][nx]) {
                                visited[ny][nx] = true;
                                q.add(new int[]{ny, nx});
                            }
                        }
                    }
                }
            }
        }

        visited = new boolean[n][n];
        List<Character> check = new ArrayList<>(List.of('R', 'G'));
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (!visited[i][j]) {
                    visited[i][j] = true;
                    strange += 1;
                    q.add(new int[]{i, j});
                    while (!q.isEmpty()) {
                        int[] r = q.poll();
                        int y = r[0], x = r[1];
                        for (int d = 0; d < 4; d++) {
                            int ny = y + dy[d];
                            int nx = x + dx[d];
                            if (ny >= 0 && ny < n && nx >= 0 && nx < n && !visited[ny][nx]
                                    && (board[y][x] == board[ny][nx] || (check.contains(board[y][x]) && check.contains(board[ny][nx])))) {
                                visited[ny][nx] = true;
                                q.add(new int[]{ny, nx});
                            }
                        }
                    }
                }
            }
        }

        System.out.println(normal + " " + strange);
    }
}
