package ps_traning.programmers.level_0;

import java.util.Arrays;

public class n번째_원소까지 {
    public int[] solution(int[] num_list, int n) {
        int[] answer = Arrays.copyOfRange(num_list, 0, n);
        return answer;
    }
}
