package ps_traning.programmers.level_0;

import java.util.ArrayList;
import java.util.List;

public class 배열_만들기_3 {
    public List<Integer> solution(int[] arr, int[][] intervals) {
        List<Integer> answer = new ArrayList<>();
        for (int[] interval : intervals) {
            for (int i = interval[0]; i < interval[1] + 1; i++) {
                answer.add(arr[i]);
            }
        }
        return answer;
    }
}
