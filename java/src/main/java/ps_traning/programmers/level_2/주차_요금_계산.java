package ps_traning.programmers.level_2;

import java.util.*;

public class 주차_요금_계산 {
    public int[] solution(int[] fees, String[] records) {
        int[] answer = {};
        Map<String, Integer> inInfo = new HashMap<>();
        Map<String, Integer> timeInfo = new HashMap<>();
        for (String record : records) {
            String[] r = record.split(" ");
            int time = 0;
            String num = r[1];
            String cmd = r[2];
            String[] temp = r[0].split(":");
            time = Integer.valueOf(temp[0]) * 60 + Integer.valueOf(temp[1]);
            if (cmd.equals("IN")) inInfo.put(num, time);
            else {
                timeInfo.put(num, timeInfo.getOrDefault(num, 0) + time - inInfo.get(num));
                inInfo.remove(num);
            }
        }
        for (String num : inInfo.keySet()) {
            timeInfo.put(num, timeInfo.getOrDefault(num, 0) + 23 * 60 + 59 - inInfo.get(num));
        }
        List<String> sortedNum = new ArrayList<>(timeInfo.keySet());
        Collections.sort(sortedNum);
        answer = new int[timeInfo.size()];

        for (int i = 0; i < timeInfo.size(); i++) {
            answer[i] += fees[1];
            String num = sortedNum.get(i);
            int time = timeInfo.get(num);
            if (time < fees[0]) continue;
            time -= fees[0];
            int per = 0;
            if (time % fees[2] != 0) per++;
            per += (int) (time / fees[2]);
            answer[i] += per * fees[3];
        }

        return answer;
    }
}
