package ps_traning.programmers.level_2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class H_index {
    public int solution(int[] citations) {
        int answer = citations.length;
        List<Integer> list = new ArrayList<>();
        for (int n : citations) {
            list.add(n);
        }
        list.sort(Collections.reverseOrder());
        for (int i = 0; i < citations.length; i++) {
            if (i + 1 > list.get(i)) {
                answer = i;
                break;
            }
        }

        return answer;
    }
}
