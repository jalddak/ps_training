package ps_traning.programmers.level_0;

import java.util.ArrayList;
import java.util.List;

public class ad_제거하기 {
    public List<String> solution(String[] strArr) {
        List<String> answer = new ArrayList<>();
        for (String str : strArr) {
            if (str.contains("ad")) {
                continue;
            }
            answer.add(str);
        }
        return answer;
    }
}
