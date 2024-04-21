package ps_traning.programmers.level_0;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class 배열의_원소_삭제하기 {
    public List<Integer> solution(int[] arr, int[] delete_list) {
        List<Integer> answer = new ArrayList<>();
        Set<Integer> d_list = new HashSet<>();
        for (int num : delete_list) {
            d_list.add(num);
        }
        for (int num : arr) {
            if (d_list.contains(num)) {
                continue;
            }
            answer.add(num);
        }

        return answer;
    }
}
