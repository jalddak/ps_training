package ps_traning.programmers.level_0;

public class 피자_나눠먹기_1 {
    public int solution(int n) {
        int answer = n / 7;
        if (n % 7 > 0) {
            answer += 1;
        }
        return answer;
    }
}
