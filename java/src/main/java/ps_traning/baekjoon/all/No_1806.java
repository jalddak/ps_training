package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class No_1806 {

    private static int n, s;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        s = Integer.parseInt(st.nextToken());

        Deque<Integer> dq = new ArrayDeque<>();

        st = new StringTokenizer(br.readLine());
        int answer = Integer.MAX_VALUE;
        int preSum = 0;
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            preSum += num;
            dq.offer(num);
            while (preSum - dq.peekFirst() >= s) {
                preSum -= dq.pollFirst();
            }
            if (preSum >= s) answer = Math.min(answer, dq.size());
        }

        System.out.println(answer == Integer.MAX_VALUE ? 0 : answer);
    }
}