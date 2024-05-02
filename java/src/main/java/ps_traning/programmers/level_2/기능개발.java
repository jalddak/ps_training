package ps_traning.programmers.level_2;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;


/**
 * 나눗셈에서 소수점 활용하려면 double로 형변환 해서 사용해야함.
 * Integer 상태에서 나누면 값도 Integer임.
 */
public class 기능개발 {
    public List<Integer> solution(int[] progresses, int[] speeds) {
        List<Integer> answer = new ArrayList<>();
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < progresses.length; i++) {
            int need = (int) Math.ceil((double) (100 - progresses[i]) / speeds[i]);
            if (queue.isEmpty() || queue.peek() >= need) {
                queue.offer(need);
                continue;
            }
            answer.add(queue.size());
            queue.clear();
            queue.offer(need);
        }
        if (!queue.isEmpty()) {
            answer.add(queue.size());
        }
        return answer;
    }
}
