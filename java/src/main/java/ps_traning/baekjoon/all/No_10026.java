package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.Queue;
import java.util.Set;

public class No_10026 {

    private static int n;
    private static char[][] board;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        board = new char[n][n];
        for (int i = 0; i < n; i++) {
            String row = br.readLine();
            for (int j = 0; j < n; j++) {
                board[i][j] = row.charAt(j);
            }
        }

        System.out.println(check(true) + " " + check(false));

    }

    private static int check(boolean normal) {
        boolean[][] visited = new boolean[n][n];
        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, 1, 0, -1};
        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j]) continue;
                visited[i][j] = true;
                result++;
                char color = board[i][j];
                Set<Character> colors = new HashSet<>();
                if (!normal && (color == 'R' || color == 'G')) {
                    colors.add('R');
                    colors.add('G');
                }
                colors.add(color);
                Queue<int[]> q = new ArrayDeque<>();
                q.add(new int[]{i, j});
                while (!q.isEmpty()) {
                    int[] poll = q.poll();
                    int y = poll[0], x = poll[1];
                    for (int d = 0; d < 4; d++) {
                        int ny = y + dy[d];
                        int nx = x + dx[d];
                        if (ny >= n || nx >= n || ny < 0 || nx < 0 || !colors.contains(board[ny][nx]) || visited[ny][nx])
                            continue;
                        visited[ny][nx] = true;
                        q.add(new int[]{ny, nx});
                    }
                }
            }
        }
        return result;
    }
}
