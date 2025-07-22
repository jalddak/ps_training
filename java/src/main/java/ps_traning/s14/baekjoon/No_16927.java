package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class No_16927 {

    private static int n, m, r;
    private static int[][] board, result;
    private static boolean[][] visited;
    private static List<Deque<Integer>> lines = new ArrayList<>();
    private static int[] dy = {1, 0, -1, 0};
    private static int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());


        n = Integer.valueOf(st.nextToken());
        m = Integer.valueOf(st.nextToken());
        r = Integer.valueOf(st.nextToken());

        board = new int[n][m];
        visited = new boolean[n][m];
        result = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.valueOf(st.nextToken());
            }
        }

        makeLine();
        round();
        makeResult();

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                sb.append(result[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.print(sb);
    }

    private static void makeResult() {
        int cnt = 0;
        int y = 0, x = 0, d = 0, li = 0;
        Deque<Integer> line = lines.get(li);

        while (cnt < n * m) {
            cnt++;
            result[y][x] = line.poll();
            int ny = y + dy[d];
            int nx = x + dx[d];
            if (ny >= n || ny < 0 || nx >= m || nx < 0 || result[ny][nx] != 0) {
                if (d == 3) {
                    d = 0;
                    li++;
                    line = lines.get(li);
                } else d++;
                ny = y + dy[d];
                nx = x + dx[d];
            }
            y = ny;
            x = nx;
        }
    }

    private static void round() {
        for (int j = 0; j < lines.size(); j++) {
            Deque<Integer> deque = lines.get(j);
            if (deque.isEmpty()) continue;
            int tr = r % deque.size();
            for (int i = 0; i < tr; i++) {
                deque.offerFirst(deque.pollLast());
            }
        }
    }

    private static void makeLine() {
        int cnt = 0;
        int y = 0, x = 0, d = 0;
        lines.add(new ArrayDeque<>());

        while (cnt < n * m) {
            cnt += 1;
            visited[y][x] = true;
            lines.get(lines.size() - 1).offer(board[y][x]);

            int ny = y + dy[d];
            int nx = x + dx[d];
            if (ny >= n || ny < 0 || nx >= m || nx < 0 || visited[ny][nx]) {
                if (d == 3) {
                    d = 0;
                    lines.add(new ArrayDeque<>());
                } else d++;
                ny = y + dy[d];
                nx = x + dx[d];
            }
            y = ny;
            x = nx;
        }
    }
}
