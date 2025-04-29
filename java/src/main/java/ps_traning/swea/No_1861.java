package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class No_1861 {
    private static final int[] dy = {-1, 0, 1, 0};
    private static final int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("#").append(tc).append(" ");
            int n = Integer.valueOf(br.readLine());
            int[][] board = new int[n][n];
            boolean[][] visited = new boolean[n][n];
            int[][] count = new int[n][n];

            for (int i = 0; i < n; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                for (int j = 0; j < n; j++) {
                    board[i][j] = Integer.valueOf(st.nextToken());
                }
            }

            int[] result = {0, 0};
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (visited[i][j]) continue;
                    visited[i][j] = true;
                    Stack<int[]> stack = new Stack<>();
                    stack.push(new int[]{i, j});
                    int cnt = 0;
                    while (!stack.isEmpty()) {
                        int[] cur = stack.pop();
                        int y = cur[0];
                        int x = cur[1];
                        cnt += 1;
                        for (int d = 0; d < 4; d++) {
                            int ny = y + dy[d];
                            int nx = x + dx[d];
                            if (ny < 0 || ny >= n || nx < 0 || nx >= n || board[ny][nx] != board[y][x] + 1) continue;
                            if (visited[ny][nx]) {
                                cnt += count[ny][nx];
                                break;
                            }
                            visited[ny][nx] = true;
                            stack.push(new int[]{ny, nx});
                        }
                    }
                    count[i][j] = cnt;
                    if (cnt >= result[1]) {
                        if (cnt > result[1] || result[0] == 0 || result[0] > board[i][j]) {
                            result[0] = board[i][j];
                        }
                        result[1] = cnt;
                    }
                }
            }
            sb.append(result[0]).append(" ").append(result[1]).append("\n");
        }
        System.out.print(sb);
    }
}
