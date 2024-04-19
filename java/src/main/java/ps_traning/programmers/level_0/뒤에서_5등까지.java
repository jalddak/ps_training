package ps_traning.programmers.level_0;

import java.util.Arrays;

public class 뒤에서_5등까지 {
    public int[] solution(int[] num_list) {
        int[] answer = {};
        Arrays.sort(num_list);
        answer = Arrays.copyOfRange(num_list, 0, 5);
        return answer;
    }
}
