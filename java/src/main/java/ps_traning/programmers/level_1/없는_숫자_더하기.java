package ps_traning.programmers.level_1;

import java.util.HashSet;
import java.util.Set;

public class 없는_숫자_더하기 {
    public int solution(int[] numbers) {
        int answer = 0;
        Set<Integer> setNums = new HashSet<>();
        for (int i = 0; i < numbers.length; i++) {
            setNums.add(numbers[i]);
        }
        for (int n = 0; n <= 9; n++) {
            if (!setNums.contains(n)) {
                answer += n;
            }
        }
        return answer;
    }
}
