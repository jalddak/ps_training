package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class No_11729 {

    private static int cnt = 0;
    private static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        recursion(n, 1, 2, 3);
        System.out.println(cnt);
        System.out.print(sb);
    }

    private static void recursion(int n, int start, int middle, int end) {
        if (n == 0) return;
        recursion(n - 1, start, end, middle);
        cnt++;
        sb.append(start).append(" ").append(end).append("\n");
        recursion(n - 1, middle, start, end);
    }


}
