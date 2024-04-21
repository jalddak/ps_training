package ps_traning.programmers.level_0;

public class 홀짝에_따라_다른_값_반환하기 {
    public int solution(int n) {
        int answer = 0;
        int num = 0;
        if (n % 2 != 0) {
            num = 1;
        } else {
            num = 2;
        }
        for (; num <= n; num += 2) {
            if (num % 2 != 0) {
                answer += num;
            } else {
                answer += num * num;
            }
        }
        return answer;
    }
}
