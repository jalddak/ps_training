package ps_traning.programmers.level_0;

import java.util.ArrayList;
import java.util.List;

public class n의_배수_고르기 {
    public int[] solution(int n, int[] numlist) {
        int[] answer = {};
        List<Integer> temp = new ArrayList<>();
        for (int num : numlist) {
            if (num % n == 0) {
                temp.add(num);
            }
        }
        answer = temp.stream().mapToInt(Integer::intValue).toArray();
        return answer;
    }
}
