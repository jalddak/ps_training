package ps_traning.programmers.level_0;

import java.util.HashSet;
import java.util.Set;

public class 글자_지우기 {
    public String solution(String my_string, int[] indices) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        Set<Integer> indicesSet = new HashSet<>();
        for (int num : indices) {
            indicesSet.add(num);
        }
        for (int i = 0; i < my_string.length(); i++) {
            if (indicesSet.contains(i)) {
                continue;
            }
            sb.append(my_string.charAt(i));
        }
        answer = sb.toString();
        return answer;
    }
}
