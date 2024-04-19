package ps_traning.programmers.level_0;

import java.util.Arrays;

public class 뒤에서_5등_위로 {
    public int[] solution(int[] num_list) {
        int[] answer = {};
        Arrays.sort(num_list);
        answer = Arrays.copyOfRange(num_list, 5, num_list.length);
        return answer;
    }
}
