package ps_traning.programmers.level_1;

import java.util.Arrays;
import java.util.Collections;

public class 정수_내림차순으로_배치하기 {
    public long solution(long n) {
        String[] strArr = String.valueOf(n).split("");
        Arrays.sort(strArr, Collections.reverseOrder());
        long answer = Long.valueOf(String.join("", strArr));
        return answer;
    }
}
