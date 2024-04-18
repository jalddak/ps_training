package ps_traning.programmers.level_0;

import java.util.Arrays;

public class 배열_자르기 {
    public int[] solution(int[] numbers, int num1, int num2) {
        int[] answer = Arrays.copyOfRange(numbers, num1, num2 + 1);
        return answer;
    }
}
