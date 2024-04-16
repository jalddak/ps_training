package ps_traning.programmers.level_0;

import java.util.ArrayList;
import java.util.List;

public class 짝수는_싫어요 {
    public int[] solution(int n) {
        List<Integer> temp = new ArrayList<>();
        for (int num = 1; num <= n; num += 2) {
            temp.add(num);
        }
        return temp.stream()
                .mapToInt(Integer::intValue)
                .toArray();
    }
}
