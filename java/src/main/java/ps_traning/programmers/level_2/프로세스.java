package ps_traning.programmers.level_2;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class 프로세스 {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        Queue<Integer> queue = new LinkedList<>();
        List<Integer> list = new ArrayList<>();
        for (int p : priorities) {
            queue.offer(p);
            list.add(p);
        }
        list.sort((i1, i2) -> i2 - i1);
        Queue<Integer> sorted = new LinkedList<>(list);

        while (!queue.isEmpty()) {
            if (sorted.peek() != queue.peek()) {
                queue.offer(queue.poll());
                location -= 1;
                if (location < 0) location += queue.size();
            } else {
                queue.poll();
                sorted.poll();
                answer++;
                if (location == 0) {
                    break;
                }
                location -= 1;
            }
        }
        return answer;
    }
}
