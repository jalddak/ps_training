package ps_traning.programmers.level_0;

public class 피자_나눠먹기_3 {
    public int solution(int slice, int n) {
        int answer = n / slice;
        if (n % slice > 0) {
            answer++;
        }
        return answer;
    }
}
