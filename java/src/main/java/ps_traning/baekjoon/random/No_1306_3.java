package ps_traning.baekjoon.random;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

/**
 * 슬라이딩 윈도우
 */
public class No_1306_3 {
    private static int n, m;
    private static int[] lights;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.valueOf(st.nextToken());
        m = Integer.valueOf(st.nextToken());

        lights = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            lights[i] = Integer.valueOf(st.nextToken());
        }

        int range = 2 * m - 1;
        Deque<Integer> deque = new ArrayDeque<>();
        for (int i = 0; i < range; i++) {
            int temp = lights[i];
            while (!deque.isEmpty() && deque.getLast() < temp) deque.pollLast();
            deque.offer(temp);
        }

        StringBuilder sb = new StringBuilder();
        sb.append(deque.peek()).append(" ");
        for (int i = 1; i < n - range + 1; i++) {
            int temp = lights[i + range - 1];
            if (deque.peek() == lights[i - 1]) deque.pollFirst();
            while (!deque.isEmpty() && deque.getLast() < temp) deque.pollLast();
            deque.offer(temp);
            sb.append(deque.peek()).append(" ");
        }
        System.out.println(sb);
    }
}
