package ps_traning.programmers.level_1;

import java.util.LinkedList;
import java.util.Queue;

public class 카드_뭉치 {
    public Queue<String> makeQueue(String[] cards) {
        Queue<String> queue = new LinkedList<>();
        for (String word : cards) {
            queue.offer(word);
        }
        return queue;
    }

    public String solution(String[] cards1, String[] cards2, String[] goal) {
        String answer = "Yes";
        Queue<String> c1 = makeQueue(cards1);
        Queue<String> c2 = makeQueue(cards2);
        for (String word : goal) {
            if (!c1.isEmpty() && c1.peek().equals(word)) {
                c1.poll();
                continue;
            }
            if (!c2.isEmpty() && c2.peek().equals(word)) {
                c2.poll();
                continue;
            }
            answer = "No";
            break;
        }
        return answer;
    }
}
