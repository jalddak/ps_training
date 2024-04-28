package ps_traning.programmers.level_2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class 구명보트 {
    public int solution(int[] people, int limit) {
        int answer = 0;
        List<Integer> pList = new ArrayList<>();
        for (int n : people) {
            pList.add(n);
        }
        Collections.sort(pList, Collections.reverseOrder());
        int last = people.length - 1;
        for (int i = 0; i <= last; i++) {
            if (pList.get(i) + pList.get(last) <= limit) {
                last--;
            }
            answer++;
        }
        return answer;
    }
}
