package ps_traning.programmers.level_1;

public class 콜라츠_추측 {
    public int solution(long num) {
        int answer = 0;
        while (num != 1) {
            if (num % 2 == 0) {
                num /= 2;
            } else {
                num *= 3;
                num += 1;
            }
            answer += 1;
            if (answer > 500) {
                answer = -1;
                break;
            }

        }
        return answer;
    }
}
