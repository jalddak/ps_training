package ps_traning.programmers.level_0;

import java.util.ArrayList;
import java.util.List;

public class 배열_만들기2 {
    public List<Integer> solution(int l, int r) {
        List<Integer> answer = new ArrayList<>();
        String[] nots = {"1", "2", "3", "4", "6", "7", "8", "9"};
        Loop:
        for (int n = l; n <= r; n++) {
            String strN = String.valueOf(n);
            for (String not : nots) {
                if (strN.contains(not)) {
                    continue Loop;
                }
            }
            answer.add(Integer.valueOf(strN));
        }
        if (answer.size() == 0) {
            answer.add(-1);
        }
        return answer;
    }
}
