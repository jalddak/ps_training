package ps_traning.programmers.level_0;

import java.util.ArrayList;
import java.util.List;

public class _5명씩 {
    public List<String> solution(String[] names) {
        List<String> answer = new ArrayList<>();
        for (int i = 0; i < names.length; i += 5) {
            answer.add(names[i]);
        }
        return answer;
    }
}
