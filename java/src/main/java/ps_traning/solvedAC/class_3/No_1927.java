package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class No_1927 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int c = Integer.parseInt(br.readLine());
            if (c == 0 && pq.isEmpty()) sb.append(0).append("\n");
            else if (c == 0) sb.append(pq.poll()).append("\n");
            else pq.offer(c);
        }
        System.out.println(sb.toString());

    }
}
