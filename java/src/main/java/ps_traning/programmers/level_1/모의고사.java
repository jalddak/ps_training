package ps_traning.programmers.level_1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class 모의고사 {
    public List<Integer> solution(int[] answers) {
        int[] cnt = {0, 0, 0};
        for (int i = 0; i < 3; i++) {
            int[] temp = {};
            if (i == 0) {
                temp = new int[]{1, 2, 3, 4, 5};
            } else if (i == 1) {
                temp = new int[]{2, 1, 2, 3, 2, 4, 2, 5};
            } else if (i == 2) {
                temp = new int[]{3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
            }
            for (int j = 0; j < answers.length; j++) {
                if (answers[j] == temp[j % temp.length]) {
                    cnt[i]++;
                }
            }
        }
        int maxCnt = Collections.max(Arrays.asList(cnt[0], cnt[1], cnt[2]));
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            if (maxCnt == cnt[i]) {
                answer.add(i + 1);
            }
        }
        return answer;
    }
}
