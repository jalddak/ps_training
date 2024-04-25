package ps_traning.programmers.level_1;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class 제일_작은_수_제거하기 {
    public int[] solution(int[] arr) {
        List<Integer> arrList = new ArrayList<>();
        for (int n : arr) {
            arrList.add(n);
        }
        arrList.remove(Collections.min(arrList));
        int[] answer = new int[arrList.size()];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = arrList.get(i);
        }
        if (answer.length == 0) {
            answer = new int[]{-1};
        }
        return answer;
    }
}
