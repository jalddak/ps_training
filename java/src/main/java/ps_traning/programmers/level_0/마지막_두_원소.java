package ps_traning.programmers.level_0;

import java.util.Arrays;

public class 마지막_두_원소 {
    public int[] solution(int[] num_list) {
        int lastIndex = num_list.length - 1;
        int[] answer = Arrays.copyOf(num_list, num_list.length + 1);
        if (num_list[lastIndex] > num_list[lastIndex - 1]) {
            answer[lastIndex + 1] = num_list[lastIndex] - num_list[lastIndex - 1];
        } else {
            answer[lastIndex + 1] = num_list[lastIndex] * 2;
        }
        return answer;
    }
}
