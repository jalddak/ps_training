package ps_traning.programmers.level_2;

import java.util.*;

public class 연속_부분_수열_합의_개수 {
    public int sum(Queue<Integer> queue, int length) {
        int result = 0;
        List<Integer> list = new ArrayList(queue);
        for (int i = 0; i < length; i++) {
            result += list.get(i);
        }
        return result;
    }

    public int solution(int[] elements) {
        int answer = 0;
        Set<Integer> set = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();
        for (int n : elements) {
            set.add(n);
            queue.offer(n);
        }
        for (int i = 0; i < elements.length; i++) {
            for (int j = 2; j < elements.length; j++) {
                set.add(sum(queue, j));
            }
            queue.offer(queue.poll());
        }

        answer = set.size() + 1;
        return answer;
    }
}
