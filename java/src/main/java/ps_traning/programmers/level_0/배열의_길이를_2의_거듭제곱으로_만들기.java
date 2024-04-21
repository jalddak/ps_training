package ps_traning.programmers.level_0;

import java.util.Arrays;

public class 배열의_길이를_2의_거듭제곱으로_만들기 {
    public int[] solution(int[] arr) {
        int[] answer = {};
        int need = 1;
        while (need < arr.length) {
            need *= 2;
        }
        answer = Arrays.copyOf(arr, need);
        return answer;
    }
}
