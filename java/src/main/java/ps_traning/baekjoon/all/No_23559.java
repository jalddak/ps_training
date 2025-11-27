package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.Stack;
import java.util.StringTokenizer;

public class No_23559 {

    private static int n, x;
    private static PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> {
        return (b[0] - b[1]) - (a[0] - a[1]);
    });

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            pq.offer(new int[]{Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())});
        }

        Stack<int[]> q = new Stack<>();
        int result = 0;
        while (!pq.isEmpty()) {
            int[] poll = pq.poll();
            int a = poll[0], b = poll[1];
            if (a > b && x >= 5000) {
                result += a;
                x -= 5000;
                q.push(poll);
            } else {
                if (x < 1000) {
                    int[] temp = q.pop();
                    result -= temp[0];
                    result += temp[1];
                    x += 4000;
                }
                result += b;
                x -= 1000;
            }
        }

        System.out.println(result);
    }
}
