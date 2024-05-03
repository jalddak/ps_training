package ps_traning.programmers.level_1;

import java.util.ArrayList;
import java.util.List;

public class 과일_장수 {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        List<Integer> list = new ArrayList<>();
        for (int s : score) {
            list.add(s);
        }
        list.sort((i1, i2) -> i2 - i1);
        for (int i = m - 1; i < score.length; i += m) {
            answer += list.get(i) * m;
        }
        return answer;
    }
}
