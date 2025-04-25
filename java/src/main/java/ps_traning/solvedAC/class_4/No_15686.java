package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class No_15686 {
    private static int n, m, answer;
    private static List<int[]> homes, chickens;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.valueOf(st.nextToken());
        m = Integer.valueOf(st.nextToken());
        answer = 101 * 2500;
        homes = new ArrayList<>();
        chickens = new ArrayList<>();

        int[][] board = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.valueOf(st.nextToken());
                if (board[i][j] == 1) homes.add(new int[]{i, j});
                else if (board[i][j] == 2) chickens.add(new int[]{i, j});
            }
        }
        int[] distances = new int[homes.size()];
        Arrays.fill(distances, 101);
        solution(0, 0, distances);
        System.out.println(answer);
    }

    private static int calcDistance(int hy, int hx, int cy, int cx) {
        return Math.abs(hy - cy) + Math.abs(hx - cx);
    }

    private static int[] checkDistances(int[] distances, int cy, int cx) {
        int len = homes.size();
        int[] result = new int[len];
        for (int i = 0; i < len; i++) {
            int hy = homes.get(i)[0], hx = homes.get(i)[1];
            result[i] = Math.min(distances[i], calcDistance(hy, hx, cy, cx));
        }
        return result;
    }

    private static void solution(int depth, int k, int[] distances) {
        if (depth == m) {
            answer = Math.min(answer, Arrays.stream(distances).sum());
            return;
        }

        for (int i = k; i < chickens.size() - m + 1 + depth; i++) {
            int cy = chickens.get(i)[0], cx = chickens.get(i)[1];
            int[] nDistances = checkDistances(distances, cy, cx);
            solution(depth + 1, i + 1, nDistances);
        }
    }
}
