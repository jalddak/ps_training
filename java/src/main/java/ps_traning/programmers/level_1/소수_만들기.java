package ps_traning.programmers.level_1;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class 소수_만들기 {
    public int solution(int[] nums) {
        int answer = 0;
        Arrays.sort(nums);
        int maxSum = 0;
        Set<Integer> set = new HashSet<>();
        for (int i = nums.length - 3; i < nums.length; i++) {
            maxSum += nums[i];
        }
        boolean[] checked = new boolean[maxSum + 1];
        for (int n = 2; n <= maxSum; n++) {
            if (checked[n]) continue;
            set.add(n);
            for (int m = n; m <= maxSum; m += n) {
                checked[m] = true;
            }
        }
        for (int i = 0; i < nums.length - 2; i++) {
            for (int j = i + 1; j < nums.length - 1; j++) {
                for (int k = j + 1; k < nums.length; k++) {
                    if (set.contains(nums[i] + nums[j] + nums[k])) {
                        answer++;
                    }
                }
            }
        }

        return answer;
    }
}
