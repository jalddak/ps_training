package ps_traning.programmers.level_1;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class 나누어_떨어지는_숫자_배열 {
    public List<Integer> solution(int[] arr, int divisor) {
        List<Integer> answer = new ArrayList<>();
        for (int n : arr) {
            if (n % divisor == 0) {
                answer.add(n);
            }
        }
        if (answer.size() == 0) {
            answer.add(-1);
        }
        Collections.sort(answer);
        return answer;
    }
}
