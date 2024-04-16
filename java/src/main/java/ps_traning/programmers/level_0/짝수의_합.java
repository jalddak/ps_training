package ps_traning.programmers.level_0;

public class 짝수의_합 {
    public int solution(int n) {
        int answer = 0;
        for (int num = 2; num <= n; num += 2) {
            answer += num;
        }
        return answer;
    }
}
