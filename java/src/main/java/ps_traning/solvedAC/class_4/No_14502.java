package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class No_14502 {
    private static int n, m, answer;
    private static int[] dy, dx;
    private static int[][] board;
    private static List<int[]> virus, clean;

    public static void main(String[] avgs) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.valueOf(st.nextToken());
        m = Integer.valueOf(st.nextToken());

        board = new int[n][m];
        clean = new ArrayList<>();
        virus = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.valueOf(st.nextToken());
                if (board[i][j] == 0) clean.add(new int[]{i, j});
                else if (board[i][j] == 2) virus.add(new int[]{i, j});
            }
        }

        dy = new int[]{-1, 0, 1, 0};
        dx = new int[]{0, 1, 0, -1};
        solution(0, new Stack<>());
        System.out.println(answer);
    }

    private static void solution(int s, Stack<Integer> result) {
        int depth = result.size();
        if (depth == 3) {
            check();
            return;
        }

        for (int i = s; i < clean.size(); i++) {
            int y = clean.get(i)[0];
            int x = clean.get(i)[1];
            board[y][x] = 1;
            result.push(i);
            solution(i + 1, result);
            result.pop();
            board[y][x] = 0;

        }
    }

    private static void check() {
        boolean[][] visited = new boolean[n][m];
        int vcount = 0;
        for (int i = 0; i < virus.size(); i++) {
            int vy = virus.get(i)[0];
            int vx = virus.get(i)[1];
            if (visited[vy][vx]) continue;
            visited[vy][vx] = true;
            Queue<int[]> queue = new LinkedList<>();
            queue.offer(new int[]{vy, vx});
            while (!queue.isEmpty()) {
                int[] qr = queue.poll();
                vcount += 1;
                int y = qr[0], x = qr[1];
                for (int d = 0; d < 4; d++) {
                    int ny = y + dy[d];
                    int nx = x + dx[d];
                    if (ny >= n || ny < 0 || nx >= m || nx < 0 || board[ny][nx] == 1 || visited[ny][nx]) continue;
                    visited[ny][nx] = true;
                    queue.offer(new int[]{ny, nx});
                }
            }
        }

        answer = Math.max(answer, clean.size() - 3 + virus.size() - vcount);
    }
}
