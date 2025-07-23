package ps_traning.barkingdog.x0C;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class No_18809 {

    private static int n, m, g, r, answer;
    private static int[][] board;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.valueOf(st.nextToken());
        m = Integer.valueOf(st.nextToken());
        g = Integer.valueOf(st.nextToken());
        r = Integer.valueOf(st.nextToken());

        board = new int[n][m];

        List<int[]> canCrd = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.valueOf(st.nextToken());
                if (board[i][j] == 2) canCrd.add(new int[]{i, j});
            }
        }

        recursion(0, canCrd, 6, new boolean[canCrd.size()], 0);
        System.out.println(answer);
    }

    // color: 3 -> green, 4 -> red, 5 -> flower, 6 -> new green, 7 -> new Red
    private static void recursion(int depth, List<int[]> canCrd, int color, boolean[] visited, int start) {
        int limit = color == 6 ? g : r;
        if (depth == limit) {
            if (color == 6) {
                recursion(0, canCrd, 7, visited, 0);
                return;
            }
            answer = Math.max(answer, solution());
        }

        int len = canCrd.size();
        for (int i = start; i < len; i++) {
            if (visited[i]) continue;
            visited[i] = true;
            int y = canCrd.get(i)[0], x = canCrd.get(i)[1];
            board[y][x] = color;
            recursion(depth + 1, canCrd, color, visited, i + 1);
            board[y][x] = 2;
            visited[i] = false;
        }


    }

    private static int solution() {
        int[][] copy = new int[n][m];
        Stack<int[]> gStack = new Stack<>();
        Stack<int[]> rStack = new Stack<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                copy[i][j] = board[i][j];
                if (copy[i][j] == 6) gStack.push(new int[]{i, j});
                else if (copy[i][j] == 7) rStack.push(new int[]{i, j});
            }
        }

        while (!gStack.isEmpty() && !rStack.isEmpty()) {
            gStack = spread(copy, gStack, 6);
            rStack = spread(copy, rStack, 7);
        }

        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (copy[i][j] == 5) result++;
            }
        }
        return result;
    }

    private static Stack<int[]> spread(int[][] copy, Stack<int[]> stack, int color) {
        int[] dy = {-1, 0, 1, 0};
        int[] dx = {0, 1, 0, -1};
        Set<Integer> canSpread = new HashSet<>();
        canSpread.add(1);
        canSpread.add(2);
        canSpread.add(6);

        Stack<int[]> result = new Stack<>();
        while (!stack.isEmpty()) {
            int[] pop = stack.pop();
            int y = pop[0], x = pop[1];
            if (copy[y][x] != color) continue;
            copy[y][x] = color - 3;
            for (int d = 0; d < 4; d++) {
                int ny = y + dy[d];
                int nx = x + dx[d];
                if (ny >= n || ny < 0 || nx >= m || nx < 0 || !canSpread.contains(copy[ny][nx])) continue;
                if (copy[ny][nx] == 6) {
                    if (color == 7) copy[ny][nx] = 5;
                    continue;
                }
                copy[ny][nx] = color;
                result.push(new int[]{ny, nx});
            }
        }
        return result;
    }
}

