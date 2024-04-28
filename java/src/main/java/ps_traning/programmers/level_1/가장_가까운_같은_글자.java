package ps_traning.programmers.level_1;

import java.util.HashMap;
import java.util.Map;

public class 가장_가까운_같은_글자 {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        Map<Character, Integer> map = new HashMap<>();
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (map.get(c) == null) {
                answer[i] = -1;
                map.put(c, i);
            } else {
                answer[i] = i - map.get(c);
                map.replace(c, i);
            }
        }
        return answer;
    }
}
