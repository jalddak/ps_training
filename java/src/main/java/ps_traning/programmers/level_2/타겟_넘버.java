package ps_traning.programmers.level_2;

import java.util.ArrayList;
import java.util.List;

public class 타겟_넘버 {
    public int solution(int[] numbers, int target) {
        int answer = 0;
        List<Integer> dp = new ArrayList<>();
        dp.add(0);

        for (Integer n : numbers) {
            List<Integer> temp = new ArrayList<>();
            for (Integer before : dp) {
                temp.add(before + n);
                temp.add(before - n);
            }
            dp = temp;
        }

        for (Integer n : dp) {
            if (target == n) {
                answer++;
            }
        }
        return answer;
    }
}
