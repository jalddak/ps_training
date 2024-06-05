package ps_traning.programmers.level_3;

import java.util.Arrays;

public class 최고의_집합 {
    public int[] solution(int n, int s) {
        int[] answer = {-1};
        if ((int) (s / n) == 0) return answer;

        answer = new int[n];
        Arrays.fill(answer, (int) (s / n));
        int index = n - 1;
        for (int i = 0; i < s % n; i++) {
            answer[index--]++;
        }
        return answer;
    }
}
