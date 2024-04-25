package ps_traning.programmers.level_2;


import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class 최댓값과_최솟값 {
    public String solution(String s) {
        String answer = "";
        List<Integer> list = new ArrayList<>();
        for (String strN : s.split(" ")) {
            list.add(Integer.valueOf(strN));
        }
        StringBuilder sb = new StringBuilder();
        sb.append(Collections.min(list));
        sb.append(" ");
        sb.append(Collections.max(list));
        answer = sb.toString();
        return answer;
    }
}
