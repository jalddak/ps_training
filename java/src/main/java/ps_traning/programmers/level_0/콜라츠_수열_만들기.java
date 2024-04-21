package ps_traning.programmers.level_0;

import java.util.ArrayList;
import java.util.List;

public class 콜라츠_수열_만들기 {
    public List<Integer> solution(int n) {
        List<Integer> answer = new ArrayList<>();
        while (n != 1) {
            answer.add(n);
            if (n % 2 == 0) {
                n /= 2;
            } else {
                n = n * 3 + 1;
            }
        }
        answer.add(n);
        return answer;
    }
}
