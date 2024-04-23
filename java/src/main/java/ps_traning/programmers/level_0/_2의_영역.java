package ps_traning.programmers.level_0;

import java.util.Arrays;

public class _2의_영역 {
    public int[] solution(int[] arr) {
        int[] answer = {};
        int start = -1;
        int last = -1;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 2) {
                if (start == -1) {
                    start = i;
                }
                last = i;
            }
        }
        if (start == -1) {
            answer = new int[]{-1};
        } else {
            answer = Arrays.copyOfRange(arr, start, last + 1);
        }
        return answer;
    }
}
