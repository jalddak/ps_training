package ps_traning.programmers.level_0;

import java.util.Collection;
import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class 문자열_묶기 {
    public int solution(String[] strArr) {
        int answer = 0;
        Map<Integer, Integer> lenMap = new HashMap<>();
        for (String str : strArr) {
            if (!lenMap.containsKey(str.length())) {
                lenMap.put(str.length(), 1);
            } else {
                lenMap.replace(str.length(), lenMap.get(str.length()) + 1);
            }
        }
        Collection<Integer> cnts = lenMap.values();
        answer = Collections.max(cnts);
        return answer;
    }
}
