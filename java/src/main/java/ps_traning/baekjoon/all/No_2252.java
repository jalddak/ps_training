package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class No_2252 {

    private static int n, m;

    private static List<Integer>[] cs;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        cs = new List[n];

        for (int i = 0; i < n; i++) {
            cs[i] = new ArrayList<>();
        }

        int[] pc = new int[n];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int p = Integer.parseInt(st.nextToken()) - 1;
            int c = Integer.parseInt(st.nextToken()) - 1;
            cs[p].add(c);
            pc[c] += 1;
        }

        Queue<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            if (pc[i] == 0) q.add(i);
        }

        StringBuilder sb = new StringBuilder();
        while (!q.isEmpty()) {
            int poll = q.poll();
            sb.append(poll + 1).append(" ");

            for (int c : cs[poll]) {
                pc[c] -= 1;
                if (pc[c] == 0) q.add(c);
            }
        }

        System.out.println(sb);
    }
}