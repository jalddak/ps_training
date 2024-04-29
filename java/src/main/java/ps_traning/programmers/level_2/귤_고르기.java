package ps_traning.programmers.level_2;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class 귤_고르기 {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for (int size : tangerine) {
            map.put(size, map.getOrDefault(size, 0) + 1);
        }
        List<Integer> cnts = new ArrayList(map.values());
//        Collections.sort(cnts, Collections.reverseOrder());
        cnts.sort((n1, n2) -> n2 - n1);
        for (int cnt : cnts) {
            k -= cnt;
            answer++;
            if (k <= 0) break;
        }
        return answer;
    }
}
