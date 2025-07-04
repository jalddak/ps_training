package ps_traning.swea;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

class No_1868_second {

    private static StringBuilder sb = new StringBuilder();
    private static int n, answer;
    private static char[][] board;
    private static boolean[][] checked, visited;

    private static int[] dy = {-1, -1, -1, 0, 1, 1, 1, 0};
    private static int[] dx = {-1, 0, 1, 1, 1, 0, -1, -1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= t; tc++) {
            sb.append("#").append(tc).append(" ");
            n = Integer.valueOf(br.readLine());
            board = new char[n][n];
            checked = new boolean[n][n];
            visited = new boolean[n][n];
            for (int i = 0; i < n; i++) board[i] = br.readLine().toCharArray();
            answer = 0;
            check();
            solution();
            sb.append(answer).append("\n");
        }
        System.out.print(sb);
    }

    private static void check() {
        for (int y = 0; y < n; y++) {
            for (int x = 0; x < n; x++) {
                if (board[y][x] != '*') continue;
                for (int d = 0; d < 8; d++) {
                    int ay = y + dy[d];
                    int ax = x + dx[d];
                    if (ay < 0 || ax < 0 || ay >= n || ax >= n || board[ay][ax] == '*' || checked[ay][ax]) continue;
                    checked[ay][ax] = true;
                    answer += 1;
                }
            }
        }
    }

    private static void solution() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == '*' || checked[i][j] || visited[i][j]) continue;
                Stack<int[]> stack = new Stack<>();
                stack.push(new int[]{i, j});
                answer += 1;
                while (!stack.isEmpty()) {
                    int[] pop = stack.pop();
                    int y = pop[0], x = pop[1];
                    for (int d = 0; d < 8; d++) {
                        int ay = y + dy[d];
                        int ax = x + dx[d];
                        if (ay < 0 || ax < 0 || ay >= n || ax >= n || board[ay][ax] == '*' || visited[ay][ax]) continue;
                        visited[ay][ax] = true;
                        if (checked[ay][ax]) {
                            answer -= 1;
                            continue;
                        }
                        stack.push(new int[]{ay, ax});
                    }
                }
            }
        }
    }
}