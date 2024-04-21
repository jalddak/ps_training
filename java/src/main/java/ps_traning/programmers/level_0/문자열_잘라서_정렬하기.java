package ps_traning.programmers.level_0;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class 문자열_잘라서_정렬하기 {
    public List<String> solution(String myString) {
        List<String> answer = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(myString, "x");
        while (st.hasMoreTokens()) {
            answer.add(st.nextToken());
        }
        Collections.sort(answer);
        return answer;
    }
}
