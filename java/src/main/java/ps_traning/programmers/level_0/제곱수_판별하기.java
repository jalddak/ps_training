package ps_traning.programmers.level_0;

public class 제곱수_판별하기 {
    public int solution(int n) {
        int answer = 0;
        double root = Math.sqrt(n);
        if (root % 1 == 0) {
            answer = 1;
        } else {
            answer = 2;
        }

        return answer;
    }
}
