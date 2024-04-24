package ps_traning.programmers.level_1;

public class 두_정수_사이의_합 {
    public long solution(int a, int b) {
        long answer = 0;
        int big = Math.max(a, b);
        int small = Math.min(a, b);
        for (int n = small; n <= big; n++) {
            answer += n;
        }
        return answer;
    }
}
