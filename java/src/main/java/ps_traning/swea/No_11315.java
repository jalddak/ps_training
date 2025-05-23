package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class No_11315 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int[] dy = {0, 1, 1, 1};
        int[] dx = {1, 1, 0, -1};

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            int n = Integer.valueOf(br.readLine());
            char[][] board = new char[n][n];
            for (int i = 0; i < n; i++) {
                board[i] = br.readLine().toCharArray();
            }
            boolean[][][] visited = new boolean[4][n][n];

            String result = "NO";

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (board[i][j] == '.') continue;
                    for (int d = 0; d < 4; d++) {
                        if (visited[d][i][j]) continue;
                        visited[d][i][j] = true;
                        int cnt = 0;
                        Stack<int[]> stack = new Stack<>();
                        stack.push(new int[]{i, j});
                        while (!stack.empty()) {
                            cnt += 1;
                            if (cnt >= 5){
                                result = "YES";
                                break;
                            }
                            int[] pop = stack.pop();
                            int y = pop[0], x = pop[1];
                            int ny = y + dy[d];
                            int nx = x + dx[d];
                            if (ny >= n || ny < 0 || nx >= n || nx < 0 || board[ny][nx] == '.' || visited[d][ny][nx]) continue;
                            visited[d][ny][nx] = true;
                            stack.push(new int[]{ny, nx});
                        }
                    }
                    if (result.equals("YES")) break;
                }
                if (result.equals("YES")) break;
            }

            sb.append("#").append(tc).append(" ").append(result).append("\n");
        }
        System.out.print(sb);
    }
}
