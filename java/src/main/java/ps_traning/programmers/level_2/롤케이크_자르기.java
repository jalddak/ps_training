package ps_traning.programmers.level_2;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class 롤케이크_자르기 {
    public int solution(int[] topping) {
        int answer = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for (int t : topping) map.put(t, map.getOrDefault(t, 0) + 1);
        int cnt = map.size();
        Set<Integer> set = new HashSet<>();
        for (int t : topping) {
            if (cnt < set.size()) break;
            map.replace(t, map.get(t) - 1);
            if (map.get(t) == 0) cnt--;
            set.add(t);
            if (cnt == set.size()) answer++;
        }


        return answer;
    }
}
