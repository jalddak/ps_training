package ps_traning.programmers.level_3;

import java.util.PriorityQueue;

public class 야근_지수 {
    public long solution(int n, int[] works) {
        long answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int w : works) pq.offer(-w);
        for (int i = 0; i < n; i++) {
            if (pq.isEmpty()) break;
            int w = pq.poll() + 1;
            if (w == 0) continue;
            pq.offer(w);
        }
        while (!pq.isEmpty()) {
            answer += Math.pow(pq.poll(), 2);
        }
        return answer;
    }
}
