package ps_traning.programmers.level_1;

import java.util.HashMap;
import java.util.Map;

public class 추억_점수 {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        int[] answer = new int[photo.length];
        Map<String, Integer> score = new HashMap<>();
        for (int i = 0; i < name.length; i++) {
            score.put(name[i], yearning[i]);
        }
        for (int i = 0; i < photo.length; i++) {
            String[] names = photo[i];
            int result = 0;
            for (String n : names) {
                result += score.getOrDefault(n, 0);
            }
            answer[i] = result;
        }
        return answer;
    }
}
