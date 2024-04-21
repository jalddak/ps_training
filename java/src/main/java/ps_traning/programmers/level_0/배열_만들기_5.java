package ps_traning.programmers.level_0;

import java.util.ArrayList;
import java.util.List;

public class 배열_만들기_5 {
    public List<Integer> solution(String[] intStrs, int k, int s, int l) {
        List<Integer> answer = new ArrayList<>();
        for (String str : intStrs) {
            int n = Integer.valueOf(str.substring(s, s + l));
            if (n > k) {
                answer.add(n);
            }
        }
        return answer;
    }
}
