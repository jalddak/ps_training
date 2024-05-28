package ps_traning.programmers.level_2;

import java.util.PriorityQueue;

public class 더_맵게 {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int s : scoville) pq.offer(s);
        while (pq.size() >= 2 && pq.peek() < K) {
            int first = pq.poll();
            int second = pq.poll();
            pq.offer(first + second * 2);
            answer++;
        }
        if (pq.peek() < K) answer = -1;
        return answer;
    }
}
