package ps_traning.programmers.level_2;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class 최솟값_만들기 {
    public int solution(int[] A, int[] B) {
        int answer = 0;
        List<Integer> aList = new ArrayList<>();
        List<Integer> bList = new ArrayList<>();
        for (int i = 0; i < A.length; i++) {
            aList.add(A[i]);
            bList.add(B[i]);
        }
        Collections.sort(aList);
        Collections.sort(bList, Collections.reverseOrder());
        for (int i = 0; i < A.length; i++) {
            answer += aList.get(i) * bList.get(i);
        }


        return answer;
    }
}
