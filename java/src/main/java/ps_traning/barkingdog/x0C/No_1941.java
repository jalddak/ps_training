package ps_traning.barkingdog.x0C;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

class No_1941 {

    private static char[][] board;
    private static boolean[][] visited;
    private static int n, answer;
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = 5;
        board = new char[n][n];
        visited = new boolean[n][n];

        for (int i = 0; i < n; i++) {
            board[i] = br.readLine().toCharArray();
        }

        recursion(0, 0, 0);
        System.out.println(answer);
    }

    private static void recursion(int depth, int y, int x) {
        if (depth == 7) {
            if (check(y, x)) answer++;
            return;
        }

        for (int i = y; i < n; i++) {
            for (int j = x; j < n; j++) {
                if (visited[i][j]) continue;
                visited[i][j] = true;
                recursion(depth + 1, i, j);
                visited[i][j] = false;
            }
            x = 0;
        }
    }

    private static boolean check(int y, int x) {
        boolean result = true;
        int cnt = 0;
        int sCnt = 0;

        Stack<int[]> stack = new Stack<>();
        stack.push(new int[]{y, x});
        boolean[][] checked = new boolean[n][n];
        checked[y][x] = true;

        while (!stack.isEmpty()) {
            int[] pop = stack.pop();
            y = pop[0];
            x = pop[1];
            cnt++;
            if (board[y][x] == 'S') sCnt++;

            for (int d = 0; d < 4; d++) {
                int ny = y + dy[d];
                int nx = x + dx[d];
                if (ny >= n || nx >= n || ny < 0 || nx < 0 || !visited[ny][nx] || checked[ny][nx]) continue;
                checked[ny][nx] = true;
                stack.push(new int[]{ny, nx});
            }

        }

        if (cnt < 7 || sCnt < 4) result = false;
        return result;
    }
}