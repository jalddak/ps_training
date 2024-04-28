package ps_traning.programmers.level_2;

import java.util.HashSet;
import java.util.Set;

public class 영어_끝말잇기 {
    public int[] solution(int n, String[] words) {
        int[] answer = {0, 0};
        String before = words[0];
        Set<String> set = new HashSet<>();
        for (int i = 1; i < words.length; i++) {
            set.add(before);
            String w = words[i];
            if (before.charAt(before.length() - 1) != w.charAt(0) || set.contains(w)) {
                answer[0] = i % n + 1;
                answer[1] = i / n + 1;
                break;
            }
            before = w;
        }

        return answer;
    }
}
