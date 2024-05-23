package ps_traning.programmers.level_1;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class 옹알이_2 {
    public int solution(String[] babbling) {
        int answer = 0;
        Set<String> set = new HashSet<>(List.of("aya", "ye", "woo", "ma"));
        for (String word : babbling) {
            String before = "";
            StringBuilder current = new StringBuilder();
            for (char c : word.toCharArray()) {
                current.append(c);
                if (set.contains(current.toString()) && !before.equals(current.toString())) {
                    before = current.toString();
                    current.setLength(0);
                }
                if (current.length() > 3) break;
            }
            if (current.length() == 0) answer++;
        }
        return answer;
    }
}
