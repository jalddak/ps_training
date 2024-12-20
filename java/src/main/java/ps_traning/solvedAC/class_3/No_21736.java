package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class No_21736 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken());
        int m = Integer.valueOf(st.nextToken());
        String[][] board = new String[n][m];
        for (int i = 0; i < n; i++) {
            board[i] = br.readLine().split("");
        }

        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, 1, 0, -1};
        boolean[][] visited = new boolean[n][m];
        int answer = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!board[i][j].equals("I")) continue;
                visited[i][j] = true;
                Stack<int[]> stack = new Stack<>();
                stack.push(new int[]{i, j});
                while (!stack.isEmpty()) {
                    int[] cord = stack.pop();
                    int y = cord[0], x = cord[1];
                    for (int d = 0; d < 4; d++) {
                        int ny = y + dy[d];
                        int nx = x + dx[d];
                        if (ny < 0 || ny >= n || nx < 0 || nx >= m || visited[ny][nx] || board[ny][nx].equals("X"))
                            continue;
                        visited[ny][nx] = true;
                        stack.push(new int[]{ny, nx});
                        if (board[ny][nx].equals("P")) answer++;
                    }
                }
            }
        }

        if (answer == 0) System.out.println("TT");
        else System.out.println(answer);
    }
}
