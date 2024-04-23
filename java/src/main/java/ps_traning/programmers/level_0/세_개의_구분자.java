package ps_traning.programmers.level_0;

import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class 세_개의_구분자 {
    public List<String> solution(String myStr) {
        List<String> answer = new ArrayList<>();

        StringTokenizer t = new StringTokenizer(myStr, "abc");
        while (t.hasMoreTokens()) {
            answer.add(t.nextToken());
        }
        if (answer.isEmpty()) {
            answer.add("EMPTY");
        }
        return answer;
    }
}
