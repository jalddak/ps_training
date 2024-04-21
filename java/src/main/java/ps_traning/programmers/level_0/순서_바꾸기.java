package ps_traning.programmers.level_0;

import java.util.ArrayList;
import java.util.List;

public class 순서_바꾸기 {
    public List<Integer> solution(int[] num_list, int n) {
        List<Integer> answer = new ArrayList<>();
        for (int i = n; i < num_list.length; i++) {
            answer.add(num_list[i]);
        }
        for (int i = 0; i < n; i++) {
            answer.add(num_list[i]);
        }
        return answer;
    }
}
