package ps_traning.algostudy._250909;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class No_2423 {

    private static int[][] board;
    private static int n, m;
    private static Map<Character, Integer> chg = new HashMap<>();
    private static int[] dy = {1, 1, 0};
    private static int[] dx = {0, 1, 1};
    private static int[] eS = {-1, 1, -1};

    public static void main(String[] args) throws IOException {
        chg.put('\\', 1);
        chg.put('/', -1);

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        board = new int[n][m];
        for (int i = 0; i < n; i++) {
            String row = br.readLine();
            for (int j = 0; j < m; j++) {
                board[i][j] = chg.get(row.charAt(j));
            }
        }

        int result = logic();
        System.out.println(result != Integer.MAX_VALUE ? result : "NO SOLUTION");

    }

    private static int logic() {
        if (n % 2 + m % 2 == 1) return Integer.MAX_VALUE;
        int result = 0;
        if (board[0][0] == -1) result += 1;
        if (board[n - 1][m - 1] == -1) result += 1;
        board[0][0] = 1;
        board[n - 1][m - 1] = 1;

        int[][] visited = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                visited[i][j] = Integer.MAX_VALUE;
            }
        }


        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        // 갯수, 모양, 방향, y, x
        pq.offer(new int[]{0, board[0][0], 1, 0, 0});
        while (!pq.isEmpty()) {
            int[] poll = pq.poll();
            int cnt = poll[0], shape = poll[1], dire = poll[2], y = poll[3], x = poll[4];
            if (visited[y][x] < cnt) continue;
            visited[y][x] = cnt;
            if (y == n - 1 && x == m - 1) break;
            for (int d = 0; d < 3; d++) {
                int ny = y + dy[d] * shape * dire;
                int nx = x + dx[d] * dire;
                int nShape = eS[d] * shape;
                int nDire = d == 0 ? dire * -1 : dire;
                int nCnt = cnt;
                if (ny >= n || nx >= m || ny < 0 || nx < 0 || visited[ny][nx] <= nCnt) continue;
                if (board[ny][nx] != nShape) nCnt++;
                visited[ny][nx] = nCnt;
                pq.offer(new int[]{nCnt, nShape, nDire, ny, nx});
            }

        }
        result += visited[n - 1][m - 1];
        return result;
    }
}
