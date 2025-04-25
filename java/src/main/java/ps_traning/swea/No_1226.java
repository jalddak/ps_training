package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class No_1226 {
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        for (int temp = 0; temp < 10; temp++) {
            int tc = Integer.valueOf(br.readLine());
            sb.append("#").append(tc).append(" ");

            int sy = 0, sx = 0, ey = 0, ex = 0;
            int[][] board = new int[16][16];
            for (int i = 0; i < 16; i++) {
                board[i] = br.readLine().chars().map(c -> c - '0').toArray();
                for (int j = 0; j < 16; j++) {
                    if (board[i][j] == 2) {
                        sy = i;
                        sx = j;
                    } else if (board[i][j] == 3) {
                        ey = i;
                        ex = j;
                    }
                }
            }
            boolean[][] visited = new boolean[16][16];
            int result = 0;

            Stack<int[]> stack = new Stack<>();
            stack.push(new int[]{sy, sx});
            visited[sy][sx] = true;

            while (!stack.isEmpty()) {
                int[] pop = stack.pop();
                int y = pop[0], x = pop[1];
                if (y == ey && x == ex) {
                    result = 1;
                    break;
                }

                for (int d = 0; d < 4; d++) {
                    int ny = y + dy[d];
                    int nx = x + dx[d];

                    if (ny < 0 || ny >= 16 || nx < 0 || nx >= 16 || visited[ny][nx] || board[ny][nx] == 1) continue;
                    stack.push(new int[]{ny, nx});
                    visited[ny][nx] = true;
                }
            }
            sb.append(result).append("\n");

        }
        System.out.print(sb);
    }
}
