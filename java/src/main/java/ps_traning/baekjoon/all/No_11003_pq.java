package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class No_11003_pq {

    private static int n, l;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
            return a[0] - b[0];
        });

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < l; i++) {
            int num = Integer.parseInt(st.nextToken());
            pq.offer(new int[]{num, i});
            sb.append(pq.peek()[0]).append(" ");
        }

        for (int i = l; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            pq.offer(new int[]{num, i});
            while (!pq.isEmpty() && i - pq.peek()[1] >= l)
                pq.poll();
            sb.append(pq.peek()[0]).append(" ");
        }

        System.out.println(sb);
    }
}