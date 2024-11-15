package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class No_1012 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.valueOf(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int a = 0; a < t; a++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int m = Integer.valueOf(st.nextToken());
            int n = Integer.valueOf(st.nextToken());
            int k = Integer.valueOf(st.nextToken());
            int[][] board = new int[n][m];
            boolean[][] visited = new boolean[n][m];

            for (int i = 0; i < k; i++) {
                st = new StringTokenizer(br.readLine());
                int x = Integer.valueOf(st.nextToken());
                int y = Integer.valueOf(st.nextToken());
                board[y][x] = 1;
            }

            int cnt = 0;
            int[] dy = {-1, 0, 1, 0};
            int[] dx = {0, 1, 0, -1};
            for (int y = 0; y < n; y++) {
                for (int x = 0; x < m; x++) {
                    if (visited[y][x]) continue;
                    visited[y][x] = true;
                    if (board[y][x] == 0) continue;
                    Stack<int[]> stack = new Stack<>();
                    stack.push(new int[]{y, x});
                    cnt += 1;
                    while (!stack.isEmpty()) {
                        int[] loca = stack.pop();
                        int cy = loca[0], cx = loca[1];
                        for (int d = 0; d < 4; d++) {
                            int ny = cy + dy[d];
                            int nx = cx + dx[d];
                            if (ny < 0 || ny >= n || nx < 0 || nx >= m) continue;
                            if (visited[ny][nx]) continue;
                            visited[ny][nx] = true;
                            if (board[ny][nx] == 1) stack.push(new int[]{ny, nx});
                        }
                    }
                }
            }
            sb.append(cnt).append("\n");
        }
        System.out.print(sb.toString());
    }
}
