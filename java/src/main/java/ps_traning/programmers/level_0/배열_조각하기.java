package ps_traning.programmers.level_0;

import java.util.Arrays;

public class 배열_조각하기 {
    public int[] solution(int[] arr, int[] query) {
        int[] answer = {};
        for (int i = 0; i < query.length; i++) {
            if (i % 2 == 0) {
                arr = Arrays.copyOfRange(arr, 0, query[i] + 1);
            } else {
                arr = Arrays.copyOfRange(arr, query[i], arr.length);
            }
        }
        answer = arr;
        return answer;
    }
}
