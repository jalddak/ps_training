package ps_traning.programmers.level_1;

import java.util.HashSet;
import java.util.Set;

public class 폰켓몬 {
    public int solution(int[] nums) {
        int answer = nums.length / 2;
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        answer = Math.min(answer, set.size());
        return answer;
    }
}
