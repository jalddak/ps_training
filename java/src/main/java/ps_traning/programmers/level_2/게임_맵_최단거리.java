package ps_traning.programmers.level_2;

import java.util.LinkedList;
import java.util.Queue;

public class 게임_맵_최단거리 {
    public int solution(int[][] maps) {
        int answer = -1;
        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, 1, 0, -1};
        int n = maps.length, m = maps[0].length;
        boolean[][] visited = new boolean[maps.length][maps[0].length];

        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{0, 0, 1});
        visited[0][0] = true;

        while (!queue.isEmpty()) {
            int[] info = queue.poll();
            int y = info[0], x = info[1], cnt = info[2];
            if (y == n - 1 && x == m - 1) {
                return cnt;
            }
            for (int d = 0; d < 4; d++) {
                int ny = y + dy[d];
                int nx = x + dx[d];
                if (ny >= 0 && ny < n && nx >= 0 && nx < m && maps[ny][nx] != 0 && !visited[ny][nx]) {
                    queue.offer(new int[]{ny, nx, cnt + 1});
                    visited[ny][nx] = true;
                }
            }
        }

        return answer;
    }
}
