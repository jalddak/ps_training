package ps_traning.programmers.level_0;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class 무작위로_K개의_수_뽑기 {
    public int[] solution(int[] arr, int k) {
        int[] answer = new int[k];
        Arrays.fill(answer, -1);
        Set<Integer> set = new HashSet<>();
        int index = 0;
        for (int i = 0; i < arr.length && set.size() < k; i++) {
            if (!set.contains(arr[i])) {
                set.add(arr[i]);
                answer[index++] = arr[i];
            }
        }
        return answer;
    }
}
