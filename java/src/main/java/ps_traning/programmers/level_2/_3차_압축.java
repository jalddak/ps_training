package ps_traning.programmers.level_2;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class _3차_압축 {
    public List<Integer> solution(String msg) {
        List<Integer> answer = new ArrayList<>();
        int start = Integer.valueOf('A');
        Map<String, Integer> dict = new HashMap<>();
        for (int i = 0; i < 26; i++) {
            dict.put(String.valueOf((char) (start + i)), i + 1);
        }

        int index = 0;
        int len = msg.length();
        int num = 27;
        String[] msgArray = msg.split("");
        while (index < len) {
            int temp = dict.get(msgArray[index]);
            StringBuilder sb = new StringBuilder();
            sb.append(msgArray[index]);
            while (index + 1 < len) {
                sb.append(msgArray[index + 1]);
                if (dict.containsKey(sb.toString())) {
                    index++;
                    temp = dict.get(sb.toString());
                    continue;
                }
                break;
            }
            answer.add(temp);
            dict.put(sb.toString(), num);
            num++;
            index++;
        }
        return answer;
    }
}
