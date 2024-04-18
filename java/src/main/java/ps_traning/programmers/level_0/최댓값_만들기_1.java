package ps_traning.programmers.level_0;

import java.util.Arrays;

public class 최댓값_만들기_1 {
    public int solution(int[] numbers) {
        int answer = 0;
        Arrays.sort(numbers);
        int len = numbers.length;
        answer = numbers[len - 1] * numbers[len - 2];
        return answer;
    }
}
