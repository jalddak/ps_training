package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class No_15686 {
    private static int n, m, MAX, answer;
    private static int[][] board;
    private static List<int[]> hs = new ArrayList<>();
    private static List<int[]> chs = new ArrayList<>();
    private static int[] distances;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        board = new int[n][n];
        MAX = (n - 1) * 2;
        answer = MAX * n * n;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                if (board[i][j] == 1) hs.add(new int[]{i, j});
                if (board[i][j] == 2) chs.add(new int[]{i, j});
            }
        }
        distances = new int[hs.size()];
        Arrays.fill(distances, MAX);

        recursion(0, 0, distances);
        System.out.println(answer);

    }

    private static void recursion(int depth, int idx, int[] distances) {
        if (depth == m) {
            answer = Math.min(answer, Arrays.stream(distances).sum());
            return;
        }
        for (int i = idx; i < chs.size() - m + depth + 1; i++) {
            int cy = chs.get(i)[0], cx = chs.get(i)[1];
            int[] nDistances = calcDistance(cy, cx, distances);
            recursion(depth + 1, i + 1, nDistances);
        }
    }

    private static int[] calcDistance(int cy, int cx, int[] distances) {
        int[] result = new int[hs.size()];
        for (int i = 0; i < hs.size(); i++) {
            int[] hcrd = hs.get(i);
            int hy = hcrd[0], hx = hcrd[1];
            result[i] = Math.min(distances[i], Math.abs(cy - hy) + Math.abs(cx - hx));
        }
        return result;
    }
}
