package ps_traning.programmers.level_0;

import java.util.ArrayList;
import java.util.List;

public class 할_일_목록 {
    public List<String> solution(String[] todo_list, boolean[] finished) {
        List<String> answer = new ArrayList<>();
        for (int i = 0; i < todo_list.length; i++) {
            if (!finished[i]) {
                answer.add(todo_list[i]);
            }
        }
        return answer;
    }
}
