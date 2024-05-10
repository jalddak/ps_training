package ps_traning.programmers.level_2;

import java.util.HashSet;
import java.util.Set;

public class 전화번호_목록 {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        Set<String> set = new HashSet<>();
        for (String num : phone_book) {
            set.add(num);
        }
        for (String num : phone_book) {
            for (int i = 1; i < num.length(); i++) {
                if (set.contains(num.substring(0, i))) {
                    return false;
                }
            }
        }
        return answer;
    }
}
