package ps_traning.programmers.level_0;

import java.util.ArrayList;
import java.util.List;

public class 배열_만들기_1 {
    public List<Integer> solution(int n, int k) {
        List<Integer> answer = new ArrayList<>();
        for (int num = k; num <= n; num += k) {
            answer.add(num);
        }
        return answer;
    }
}
