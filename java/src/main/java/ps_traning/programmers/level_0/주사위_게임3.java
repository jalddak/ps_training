package ps_traning.programmers.level_0;

import java.util.*;

public class 주사위_게임3 {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(a, map.getOrDefault(a, 0) + 1);
        map.put(b, map.getOrDefault(b, 0) + 1);
        map.put(c, map.getOrDefault(c, 0) + 1);
        map.put(d, map.getOrDefault(d, 0) + 1);
        if (map.size() == 1) {
            answer = a * 1111;
        } else if (map.size() == 2) {
            List<Integer> scores = new ArrayList<>(map.keySet());
            if (map.get(scores.get(0)) == 3) {
                answer = (10 * scores.get(0) + scores.get(1)) * (10 * scores.get(0) + scores.get(1));
            } else if (map.get(scores.get(0)) == 1) {
                answer = (10 * scores.get(1) + scores.get(0)) * (10 * scores.get(1) + scores.get(0));
            } else if (map.get(scores.get(0)) == 2) {
                answer = (scores.get(0) + scores.get(1)) * Math.abs(scores.get(0) - scores.get(1));
            }
        } else if (map.size() == 3) {
            List<Integer> scores = new ArrayList<>(map.keySet());
            answer = 1;
            for (int i = 0; i < 3; i++) {
                if (map.get(scores.get(i)) == 2) {
                    continue;
                }
                answer *= scores.get(i);
            }
        } else {
            answer = Collections.min(Arrays.asList(a, b, c, d));
        }
        return answer;
    }
}
