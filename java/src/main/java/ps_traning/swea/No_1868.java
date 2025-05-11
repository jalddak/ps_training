package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class No_1868 {

    private static int[] dy = {-1, -1, -1, 0, 1, 1, 1, 0};
    private static int[] dx = {-1, 0, 1, 1, 1, 0, -1, -1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("#").append(tc).append(" ");
            int n = Integer.valueOf(br.readLine());
            char[][] board = new char[n][n];
            for (int i = 0; i < n; i++) {
                board[i] = br.readLine().toCharArray();
            }
            boolean[][] visited = new boolean[n][n];

            int result = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (visited[i][j] || board[i][j] == '*') continue;
                    Stack<int[]> temp = new Stack<>();
                    int cnt = checkAround(board, visited, n, i, j, temp);
                    if (cnt != 0) continue;
                    result += 1;
                    visited[i][j] = true;

                    Stack<int[]> stack = new Stack<>();
                    while (!temp.isEmpty()) {
                        int[] pop = temp.pop();
                        int y = pop[0];
                        int x = pop[1];
                        visited[y][x] = true;
                        stack.push(pop);
                    }

                    while (!stack.isEmpty()) {
                        int[] pop = stack.pop();
                        int y = pop[0];
                        int x = pop[1];

                        temp = new Stack<>();
                        cnt = checkAround(board, visited, n, y, x, temp);
                        if (cnt != 0) continue;

                        while (!temp.isEmpty()) {
                            pop = temp.pop();
                            y = pop[0];
                            x = pop[1];
                            visited[y][x] = true;
                            stack.push(pop);
                        }
                    }
                }
            }

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (visited[i][j] || board[i][j] == '*') continue;
                    result++;
                }
            }
            sb.append(result).append("\n");
        }
        System.out.print(sb.toString());

    }

    private static int checkAround(char[][] board, boolean[][] visited, int n, int y, int x, Stack<int[]> temp) {
        int cnt = 0;
        for (int d = 0; d < 8; d++) {
            int ay = y + dy[d];
            int ax = x + dx[d];
            if (ay >= n || ay < 0 || ax >= n || ax < 0 || visited[ay][ax]) continue;
            if (board[ay][ax] == '*') {
                cnt++;
                continue;
            }
            temp.add(new int[]{ay, ax});
        }
        return cnt;
    }
}
