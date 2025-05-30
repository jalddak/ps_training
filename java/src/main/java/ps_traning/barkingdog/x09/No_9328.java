package ps_traning.barkingdog.x09;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.Stack;
import java.util.StringTokenizer;

public class No_9328 {
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};
    private static Set<Character> lower, upper;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        lower = new HashSet<>();
        upper = new HashSet<>();
        for (int i = 0; i < 26; i++) {
            lower.add((char) ('a' + i));
            upper.add((char) ('A' + i));
        }

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 0; tc < tcCnt; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int h = Integer.valueOf(st.nextToken());
            int w = Integer.valueOf(st.nextToken());

            char[][] board = new char[h][w];
            boolean[][] visited = new boolean[h][w];

            Stack<int[]> stack = new Stack<>();
            for (int i = 0; i < h; i++) {
                board[i] = br.readLine().toCharArray();
                if (board[i][0] != '*' && !visited[i][0]) {
                    visited[i][0] = true;
                    stack.add(new int[]{i, 0});
                }
                if (board[i][w - 1] != '*' && !visited[i][w - 1]) {
                    visited[i][w - 1] = true;
                    stack.add(new int[]{i, w - 1});
                }
            }
            for (int i = 0; i < w; i++) {
                if (board[0][i] != '*' && !visited[0][i]) {
                    visited[0][i] = true;
                    stack.add(new int[]{0, i});
                }
                if (board[h - 1][i] != '*' && !visited[h - 1][i]) {
                    visited[h - 1][i] = true;
                    stack.add(new int[]{h - 1, i});
                }
            }
            Set<Character> key = new HashSet<>();
            String keyInput = br.readLine();
            for (char k : keyInput.toCharArray()) {
                if (k == '0') break;
                key.add(k);
            }
            int result = 0;
            boolean flag = true;
            while (flag) {
                flag = false;
                Stack<int[]> next = new Stack<>();
                while (!stack.isEmpty()) {
                    int[] pop = stack.pop();
                    int y = pop[0], x = pop[1];
                    if (upper.contains(board[y][x]) && !key.contains((char) ((int) board[y][x] + 32))) {
                        next.add(new int[]{y, x});
                        continue;
                    }
                    if (lower.contains(board[y][x])) {
                        flag = true;
                        key.add(board[y][x]);
                    }
                    if (board[y][x] == '$') {
                        result++;
                    }
                    for (int d = 0; d < 4; d++) {
                        int ny = y + dy[d];
                        int nx = x + dx[d];
                        if (ny >= h || ny < 0 || nx >= w || nx < 0 || board[ny][nx] == '*' || visited[ny][nx]) continue;
                        visited[ny][nx] = true;
                        stack.add(new int[]{ny, nx});
                    }
                }
                stack = next;
            }

            sb.append(result).append("\n");
        }
        System.out.print(sb);
    }
}
