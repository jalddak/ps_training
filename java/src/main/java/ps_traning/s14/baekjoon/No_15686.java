package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class No_15686 {

    private static int n, m, answer;
    private static List<int[]> hs, cs;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        answer = Integer.MAX_VALUE;

        hs = new ArrayList<>();
        cs = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int num = Integer.parseInt(st.nextToken());
                if (num == 1) hs.add(new int[]{i, j});
                if (num == 2) cs.add(new int[]{i, j});
            }
        }

        int[] distances = new int[hs.size()];
        Arrays.fill(distances, Integer.MAX_VALUE);
        recursion(0, distances, 0);
        System.out.println(answer);
    }

    public static int[] calcDistances(int[] distances, int cy, int cx) {
        int[] result = new int[hs.size()];
        for (int i = 0; i < hs.size(); i++) {
            int hy = hs.get(i)[0], hx = hs.get(i)[1];
            result[i] = Math.min(distances[i], Math.abs(cy - hy) + Math.abs(cx - hx));
        }
        return result;
    }

    private static void recursion(int depth, int[] distances, int idx) {
        if (depth == m) {
            answer = Math.min(answer, Arrays.stream(distances).sum());
            return;
        }

        for (int i = idx; i < cs.size(); i++) {
            int cy = cs.get(i)[0], cx = cs.get(i)[1];
            int[] nDistances = calcDistances(distances, cy, cx);
            recursion(depth + 1, nDistances, i + 1);
        }
    }
}