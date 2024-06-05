package ps_traning.programmers.level_1;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class 로또의_최고_순위와_최저_순위 {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int per = 0;
        int check = 0;
        Map<Integer, Integer> rank = new HashMap<>();
        List<Integer> wnList = new ArrayList<>();
        for (int num : win_nums) wnList.add(num);
        rank.put(6, 1);
        rank.put(5, 2);
        rank.put(4, 3);
        rank.put(3, 4);
        rank.put(2, 5);
        rank.put(1, 6);
        rank.put(0, 6);
        for (int num : lottos) {
            if (num == 0) per++;
            if (wnList.contains(num)) check++;
        }
        answer[1] = rank.get(check);
        answer[0] = rank.get(check + per);
        return answer;
    }
}
