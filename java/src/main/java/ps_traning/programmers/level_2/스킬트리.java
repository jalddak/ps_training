package ps_traning.programmers.level_2;

import java.util.HashSet;
import java.util.Set;

public class 스킬트리 {
    public int solution(String skill, String[] skill_trees) {
        int answer = 0;
        Set<Character> set = new HashSet<>();
        for (char s : skill.toCharArray()) set.add(s);
        for (String st : skill_trees) {
            StringBuilder sb = new StringBuilder(skill);
            sb = sb.reverse();
            int index = sb.length() - 1;
            for (char s : st.toCharArray()) {
                if (set.contains(s)) {
                    if (sb.charAt(index) == s) sb.setLength(index--);
                    else {
                        answer--;
                        break;
                    }
                }
            }
            answer++;
        }
        return answer;
    }
}
