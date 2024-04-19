package ps_traning.programmers.level_0;

import java.util.ArrayList;
import java.util.List;

public class x_사이의_개수 {
    public List<Integer> solution(String myString) {
        List<Integer> answer = new ArrayList<>();
        int index = 0;
        for (char c : myString.toCharArray()) {
            if (c == 'x') {
                answer.add(index);
                index = 0;
            } else {
                index += 1;
            }
        }
        answer.add(index);
        return answer;
    }
}
