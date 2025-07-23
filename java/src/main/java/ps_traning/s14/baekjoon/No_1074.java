package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_1074 {

    private static int answer;
    private static int[][] weight = {{0, 1}, {2, 3}};

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.valueOf(st.nextToken());
        int r = Integer.valueOf(st.nextToken());
        int c = Integer.valueOf(st.nextToken());
        recursion(n, r, c);
        System.out.println(answer);

    }

    private static void recursion(int n, int r, int c) {
        if (n == 0) return;
        int len = (int) Math.pow(2, n);
        int half = len / 2;
        answer += half * half * weight[r / half][c / half];
        recursion(n - 1, r % half, c % half);
    }
}