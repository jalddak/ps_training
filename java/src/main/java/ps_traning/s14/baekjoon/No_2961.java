package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_2961 {

    private static int n, result;
    private static int[][] infos;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        infos = new int[n][2];
        result = 1000000000;
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 2; j++) infos[i][j] = Integer.parseInt(st.nextToken());
        }

        recursion(0, 0, 1, 0);
        System.out.println(result);
    }

    // s : 신 / b : 쓴
    private static void recursion(int depth, int idx, int s, int b) {
        if (depth != 0)
            result = Math.min(result, Math.abs(s - b));
        for (int i = idx; i < n; i++) {
            recursion(depth + 1, i + 1, s * infos[i][0], b + infos[i][1]);
        }
    }
}