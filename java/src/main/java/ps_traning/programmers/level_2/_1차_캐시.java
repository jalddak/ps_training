package ps_traning.programmers.level_2;

import java.util.LinkedList;
import java.util.Queue;

public class _1차_캐시 {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        Queue<String> queue = new LinkedList<>();
        for (String city : cities) {
            city = city.toLowerCase();
            if (queue.contains(city)) {
                queue.remove(city);
                answer += 1;
            } else {
                answer += 5;
            }
            queue.offer(city);
            if (queue.size() > cacheSize) {
                queue.poll();
            }
        }
        return answer;
    }
}
