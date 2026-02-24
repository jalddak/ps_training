package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class No_15678 {

    private static int n, d;
    private static int[] arr;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        d = Integer.parseInt(st.nextToken());

        arr = new int[n + 1];
        st = new StringTokenizer(br.readLine());

        long answer = Long.MIN_VALUE;
        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            answer = Math.max(answer, arr[i]);
        }

        Deque<long[]> dq = new ArrayDeque<>();
        dq.offer(new long[]{0, 0});

        for (int i = 1; i <= n; i++) {
            if (!dq.isEmpty() && i - dq.peekFirst()[0] > d)
                dq.pollFirst();

            long temp = dq.peekFirst()[1] + arr[i];
            if (!dq.isEmpty() && temp < 0) {
                dq.offer(new long[]{i, 0});
                continue;
            }
            while (!dq.isEmpty() && dq.peekLast()[1] <= temp)
                dq.pollLast();
            dq.offer(new long[]{i, temp});
            answer = Math.max(answer, temp);
        }

        System.out.println(answer);
    }
}
