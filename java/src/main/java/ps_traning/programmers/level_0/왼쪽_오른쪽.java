package ps_traning.programmers.level_0;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class 왼쪽_오른쪽 {
    public String[] solution(String[] str_list) {
        String[] answer = {};
        List<String> sl = new ArrayList<>(Arrays.asList(str_list));
        int li = sl.indexOf("l");
        int ri = sl.indexOf("r");
        if (li != -1 && (li < ri || ri == -1)) {
            answer = Arrays.copyOf(str_list, li);
        } else if (ri != -1 && (ri < li || li == -1)) {
            answer = Arrays.copyOfRange(str_list, ri + 1, str_list.length);
        }
        return answer;
    }
}
