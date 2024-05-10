package ps_traning.programmers.level_2;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class _1차_뉴스_클러스터링 {
    public List<String> makeList(String str) {
        str = str.toLowerCase();
        List<String> result = new ArrayList<>();
        for (int i = 0; i < str.length() - 1; i++) {
            if (Character.isLowerCase(str.charAt(i)) && Character.isLowerCase(str.charAt(i + 1))) {
                result.add(str.substring(i, i + 2));
            }
        }
        return result;
    }

    public Map<String, Integer> makeMap(List<String> l) {
        Map<String, Integer> result = new HashMap<>();
        for (String word : l) {
            result.put(word, result.getOrDefault(word, 0) + 1);
        }

        return result;
    }

    public int solution(String str1, String str2) {
        int answer = 0;
        List<String> l1 = makeList(str1);
        List<String> l2 = makeList(str2);
        Map<String, Integer> m1 = makeMap(l1);
        Map<String, Integer> m2 = makeMap(l2);
        int inter = 0;
        int union = 0;
        for (String key : m1.keySet()) {
            if (m2.containsKey(key)) {
                int temp = Math.min(m1.get(key), m2.get(key));
                inter += temp;
                union += temp;
                m1.replace(key, m1.get(key) - temp);
                m2.replace(key, m2.get(key) - temp);
            }
            union += m1.get(key);
        }
        for (String key : m2.keySet()) {
            union += m2.get(key);
        }
        System.out.println(inter + " " + union);
        if (union == 0) answer = 65536;
        else answer = (int) (((double) inter / union) * 65536);
        return answer;
    }
}
