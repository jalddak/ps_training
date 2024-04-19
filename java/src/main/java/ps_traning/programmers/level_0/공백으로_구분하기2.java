package ps_traning.programmers.level_0;

import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class 공백으로_구분하기2 {
    public List<String> solution(String my_string) {
        List<String> answer = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(my_string);
        while (st.hasMoreTokens()) {
            answer.add(st.nextToken());
        }
        return answer;
    }
}
