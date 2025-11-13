package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class No_2423 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] board = new int[n][m];
        for (int i = 0; i < n; i++) {
            char[] temp = br.readLine().toCharArray();
            for (int j = 0; j < m; j++) {
                if (temp[j] == '/') board[i][j] = 1;
                else board[i][j] = 0;
            }
        }

        if ((n % 2 == 0 && m % 2 == 1) || (n % 2 == 1 && m % 2 == 0)) {
            System.out.println("NO SOLUTION");
            return;
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            return a[0] - b[0];
        });

        int[][] visited = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) visited[i][j] = n * m;
        }

        int[][][] dy = {
                {{0, 1, 1}, {0, -1, -1}},
                {{-1, -1, 0}, {1, 1, 0}}
        };

        int[][][] dx = {
                {{1, 1, 0}, {-1, -1, 0}},
                {{0, 1, 1}, {0, -1, -1}}
        };

        int[][][] ds = {
                {{1, 0, 1}, {1, 0, 1}},
                {{0, 1, 0}, {0, 1, 0}}
        };

        int[][][] dd = {
                {{0, 0, 1}, {1, 1, 0}},
                {{1, 0, 0}, {0, 1, 1}}
        };

        visited[0][0] = board[0][0] == 0 ? 0 : 1;
        int result = 0;
        // cnt, shape, drt, y, x
        pq.offer(new int[]{visited[0][0], 0, 0, 0, 0});
        while (!pq.isEmpty()) {
            int[] poll = pq.poll();
            int cnt = poll[0], shape = poll[1], drt = poll[2], y = poll[3], x = poll[4];
            if (y == n - 1 && x == m - 1) {
                result = cnt;
                break;
            }
            if (visited[y][x] < cnt) continue;
            for (int d = 0; d < 3; d++) {
                int ny = y + dy[shape][drt][d];
                int nx = x + dx[shape][drt][d];
                int nShape = ds[shape][drt][d];
                int nDrt = dd[shape][drt][d];
                if (ny >= n || nx >= m || ny < 0 || nx < 0) continue;
                int nCnt = cnt + (nShape == board[ny][nx] ? 0 : 1);
                if (visited[ny][nx] <= nCnt) continue;
                visited[ny][nx] = nCnt;
                pq.offer(new int[]{nCnt, nShape, nDrt, ny, nx});
            }
        }

        System.out.println(result);
    }
}
