package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class No_1227 {
    private static final int[] dy = {-1, 0, 1, 0};
    private static final int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = 10;
        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("#").append(tc).append(" ");
            tc = Integer.valueOf(br.readLine());
            int[][] board = new int[100][100];
            int sy = -1, sx = -1, ey = -1, ex = -1;
            for (int i = 0; i < 100; i++) {
                board[i] = br.readLine().chars().map(x -> x - '0').toArray();
                for (int j = 0; j < 100; j++) {
                    if (board[i][j] == 2) {
                        sy = i;
                        sx = j;
                    } else if (board[i][j] == 3) {
                        ey = i;
                        ex = j;
                    }
                }
            }
            boolean[][] visited = new boolean[100][100];
            Stack<int[]> stack = new Stack<>();
            stack.push(new int[]{sy, sx});
            visited[sy][sx] = true;
            int result = 0;
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
                    if (ny >= 100 || ny < 0 || nx >= 100 || nx < 0 || visited[ny][nx] || board[ny][nx] == 1) continue;
                    visited[ny][nx] = true;
                    stack.push(new int[]{ny, nx});
                }
            }
            sb.append(result).append("\n");
        }
        System.out.print(sb);
    }
}
