package ps_traning.programmers.level_2;

import java.util.ArrayList;
import java.util.List;

public class 튜플 {
    public List<Integer> solution(String s) {
        String[] temp = s.substring(2, s.length() - 2).replace("},{", " ").split(" ");
        List<int[]> list = new ArrayList<>();
        for (String str : temp) {
            String[] strArr = str.split(",");
            int[] intArr = new int[strArr.length];
            for (int i = 0; i < strArr.length; i++) {
                intArr[i] = Integer.valueOf(strArr[i]);
            }
            list.add(intArr);
        }
        list.sort((a1, a2) -> a1.length - a2.length);

        List<Integer> answer = new ArrayList<>();
        for (int[] intArr : list) {
            List<Integer> copy = new ArrayList<>(answer);
            for (int num : intArr) {
                if (copy.contains(num)) {
                    copy.remove((Integer) num);
                } else {
                    answer.add(num);
                    break;
                }
            }
        }
        return answer;
    }
}
