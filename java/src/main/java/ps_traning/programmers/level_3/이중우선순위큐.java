package ps_traning.programmers.level_3;

import java.util.Collections;
import java.util.PriorityQueue;

public class 이중우선순위큐 {
    public int[] solution(String[] operations) {
        int[] answer = {0, 0};
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        PriorityQueue<Integer> rpq = new PriorityQueue<>(Collections.reverseOrder());

        for (String op : operations) {
            String[] temp = op.split(" ");
            String command = temp[0];
            int num = Integer.valueOf(temp[1]);

            if (command.equals("I")) {
                pq.offer(num);
                rpq.offer(num);
            } else if (command.equals("D")) {
                if (num == -1 && !pq.isEmpty()) {
                    rpq.remove(pq.poll());
                } else if (num == 1 && !rpq.isEmpty()) {
                    pq.remove(rpq.poll());
                }
            }
        }

        if (!pq.isEmpty()) {
            answer[0] = rpq.peek();
            answer[1] = pq.peek();
        }

        return answer;
    }
}
