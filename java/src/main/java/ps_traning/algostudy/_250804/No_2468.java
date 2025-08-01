package ps_traning.algostudy._250804;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;
import java.util.StringTokenizer;

public class No_2468 {

    /**
     * n: 입력으로 주어지는 board 한변의 길이
     * result: 출력 결과
     * dy, dx => 방향 탐색 도우미
     */
    private static int n, result;
    private static int[][] board;
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        n = Integer.parseInt(br.readLine());
        board = new int[n][n];

        /**
         * maxH, minH 설정 이유:
         * 1 ~ 100 까지가 높이 제한인데, 코드 탐색하는게 완탐형식이라서 시간을 더 줄이기 위해서.
         * 최소높이부터 최대높이 직전까지만 체크하면 시간이 더 줄 것 같아서.
         */
        int maxH = 1;
        int minH = 100;

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                maxH = Math.max(maxH, board[i][j]);
                minH = Math.min(minH, board[i][j]);
            }
        }

        result = 1;
        for (int h = minH; h < maxH; h++) {
            int candidate = check(h);
            result = Math.max(result, candidate);
        }
        bw.write(String.valueOf(result));
        bw.flush();
    }

    private static int check(int h) {
        // result: 안전구역 갯수
        int result = 0;

        // visited: 방문 위치 기억
        boolean[][] visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] <= h || visited[i][j]) continue;
                visited[i][j] = true;
                result += 1;
                
                // stack을 활용한 dfs 방식 사용
                Stack<int[]> stack = new Stack<>();
                stack.push(new int[]{i, j});
                while (!stack.isEmpty()) {
                    int[] pop = stack.pop();
                    int y = pop[0], x = pop[1];
                    for (int d = 0; d < 4; d++) {
                        int ny = y + dy[d];
                        int nx = x + dx[d];
                        if (ny >= n || nx >= n || ny < 0 || nx < 0 || board[ny][nx] <= h || visited[ny][nx]) continue;
                        visited[ny][nx] = true;
                        stack.push(new int[]{ny, nx});
                    }
                }
            }
        }

        return result;
    }
}
