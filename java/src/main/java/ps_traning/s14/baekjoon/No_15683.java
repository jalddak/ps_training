package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_15683 {

    private static int n, m, k, answer;
    private static int[][] board;
    private static List<int[]> cctvs = new ArrayList<>();
    private static int[] dy = {-1, 0, 1, 0};
    private static int[] dx = {0, 1, 0, -1};
    private static Set<Integer>[] dires;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] >= 1 && board[i][j] <= 5) cctvs.add(new int[]{i, j});
            }
        }

        k = cctvs.size();
        dires = new Set[k];
        for (int i = 0; i < k; i++) {
            dires[i] = new HashSet<>();
        }

        for (int[] cctv : cctvs) {
            int y = cctv[0], x = cctv[1];
            if (board[y][x] != 5) continue;
            for (int d = 0; d < 4; d++) {
                int ny = y, nx = x;
                while (true) {
                    ny += dy[d];
                    nx += dx[d];
                    if (ny >= n || nx >= m || ny < 0 || nx < 0 || board[ny][nx] == 6) break;
                    if (board[ny][nx] != 0) continue;
                    board[ny][nx] = 7;
                }
            }
        }

        answer = Integer.MAX_VALUE;
        recursion(0);
        System.out.println(answer);

    }

    private static void recursion(int depth) {
        if (depth == k) {
            int[][] temp = drow();
            int result = 0;
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (temp[i][j] == 0) result++;
                }
            }
            answer = Math.min(answer, result);
            return;
        }

        int y = cctvs.get(depth)[0], x = cctvs.get(depth)[1];
        switch (board[y][x]) {
            case 1:
                for (int d = 0; d < 4; d++) {
                    dires[depth].add(d);
                    recursion(depth + 1);
                    dires[depth].remove(d);
                }
                break;
            case 2:
                for (int d = 0; d < 2; d++) {
                    dires[depth].add(d);
                    dires[depth].add(d + 2);
                    recursion(depth + 1);
                    dires[depth].remove(d + 2);
                    dires[depth].remove(d);
                }
                break;
            case 3:
                for (int d = 0; d < 4; d++) {
                    int nd = d != 3 ? d + 1 : 0;
                    dires[depth].add(d);
                    dires[depth].add(nd);
                    recursion(depth + 1);
                    dires[depth].remove(nd);
                    dires[depth].remove(d);
                }
                break;
            case 4:
                for (int d = 0; d < 4; d++) {
                    dires[depth].add(d);
                }
                for (int d = 0; d < 4; d++) {
                    dires[depth].remove(d);
                    recursion(depth + 1);
                    dires[depth].add(d);
                }
                break;
            case 5:
                recursion(depth + 1);
                break;
        }
    }

    private static int[][] drow() {
        int[][] result = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                result[i][j] = board[i][j];
            }
        }

        for (int i = 0; i < k; i++) {
            int y = cctvs.get(i)[0], x = cctvs.get(i)[1];
            for (int d : dires[i]) {
                int ny = y, nx = x;
                while (true) {
                    ny += dy[d];
                    nx += dx[d];
                    if (ny >= n || nx >= m || ny < 0 || nx < 0 || result[ny][nx] == 6) break;
                    result[ny][nx] = 7;
                }
            }
        }

        return result;
    }
}
