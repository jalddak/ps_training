package ps_traning.programmers.level_1;

public class 콜라_문제 {
    public int solution(int a, int b, int n) {
        int answer = 0;
        while (n >= a) {
            int change = (int) (n / a) * b;
            answer += change;
            n = n % a + change;
        }
        return answer;
    }
}
