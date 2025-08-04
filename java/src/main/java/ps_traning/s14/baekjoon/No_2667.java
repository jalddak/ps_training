package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class No_2667 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int[][] board = new int[n][n];
        for (int i = 0; i < n; i++) {
            board[i] = br.readLine().chars().map(a -> a - '0').toArray();
        }

        boolean[][] visited = new boolean[n][n];
        List<Integer> result = new ArrayList<>();
        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, 1, 0, -1};

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 0 || visited[i][j]) continue;
                visited[i][j] = true;
                Queue<int[]> q = new ArrayDeque<>();
                q.offer(new int[]{i, j});
                int cnt = 0;
                while (!q.isEmpty()) {
                    int[] poll = q.poll();
                    cnt += 1;
                    int y = poll[0], x = poll[1];
                    for (int d = 0; d < 4; d++) {
                        int ny = y + dy[d];
                        int nx = x + dx[d];
                        if (ny >= n || nx >= n || ny < 0 || nx < 0 || board[ny][nx] == 0 || visited[ny][nx]) continue;
                        visited[ny][nx] = true;
                        q.offer(new int[]{ny, nx});
                    }
                }
                result.add(cnt);
            }
        }

        result.sort(Comparator.naturalOrder());
        StringBuilder sb = new StringBuilder();
        sb.append(result.size()).append("\n");
        for (int i = 0; i < result.size(); i++) {
            sb.append(result.get(i)).append("\n");
        }
        System.out.print(sb);
    }
}