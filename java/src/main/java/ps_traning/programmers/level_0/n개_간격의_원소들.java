package ps_traning.programmers.level_0;

import java.util.ArrayList;
import java.util.List;

public class n개_간격의_원소들 {
    public List<Integer> solution(int[] num_list, int n) {
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < num_list.length; i += n) {
            answer.add(num_list[i]);
        }
        return answer;
    }
}
