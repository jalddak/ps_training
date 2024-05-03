package ps_traning.programmers.level_1;

public class 기사단원의_무기 {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        for (int num = 1; num <= number; num++) {
            int cnt = 0;
            for (int n = 1; n <= Math.sqrt(num); n++) {
                if (num % n != 0) continue;
                if (num / n != n) cnt++;
                cnt++;
            }
            if (cnt > limit) {
                cnt = power;
            }
            answer += cnt;
        }
        return answer;
    }
}
