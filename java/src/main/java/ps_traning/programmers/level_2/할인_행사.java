package ps_traning.programmers.level_2;

import java.util.Arrays;
import java.util.Collections;

public class 할인_행사 {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        for (int i = 10; i <= discount.length; i++) {
            String[] temps = Arrays.copyOfRange(discount, i - 10, i);
            boolean flag = true;
            for (int j = 0; j < want.length; j++) {
                String item = want[j];
                if (Collections.frequency(Arrays.asList(temps), item) != number[j]) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                answer++;
            }
        }
        return answer;
    }
}
