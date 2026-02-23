package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class No_11003 {

    private static int n, l;
    private static int[] a;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());

        a = new int[n];

        st = new StringTokenizer(br.readLine());
        Deque<Integer> dq = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            a[i] = num;

            if (!dq.isEmpty() && !(dq.peekFirst() > i - l))
                dq.pollFirst();

            while (!dq.isEmpty() && a[dq.peekLast()] >= num) {
                dq.pollLast();
            }
            dq.offer(i);

            sb.append(a[dq.peekFirst()]).append(" ");
        }

        System.out.println(sb);


    }
}