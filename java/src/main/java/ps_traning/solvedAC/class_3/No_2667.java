package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class No_2667 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int[][] board = new int[n][n];
        for (int i = 0; i < n; i++) {
            char[] input = br.readLine().toCharArray();
            for (int j = 0; j < n; j++) {
                board[i][j] = input[j] - '0';
            }
        }
        boolean[][] visited = new boolean[n][n];
        List<Integer> cnts = new ArrayList<>();
        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, 1, 0, -1};

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 0 || visited[i][j]) continue;
                visited[i][j] = true;
                Stack<int[]> stack = new Stack<>();
                stack.push(new int[]{i, j});
                int cnt = 0;
                while (!stack.isEmpty()) {
                    int[] temp = stack.pop();
                    int y = temp[0], x = temp[1];
                    cnt += 1;
                    for (int d = 0; d < 4; d++) {
                        int ny = y + dy[d];
                        int nx = x + dx[d];
                        if (ny >= 0 && nx >= 0 && ny < n && nx < n && board[ny][nx] == 1 && !visited[ny][nx]) {
                            stack.push(new int[]{ny, nx});
                            visited[ny][nx] = true;
                        }
                    }
                }
                cnts.add(cnt);
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append(cnts.size()).append("\n");
        cnts.sort(Integer::compareTo);
        for (int cnt : cnts) {
            sb.append(cnt).append("\n");
        }
        System.out.print(sb.toString());
    }
}
