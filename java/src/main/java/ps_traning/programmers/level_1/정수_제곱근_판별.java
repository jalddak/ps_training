package ps_traning.programmers.level_1;

public class 정수_제곱근_판별 {
    public long solution(long n) {
        long answer = -1;
        double root = Math.sqrt(n);
        if (root % (long) root == 0) {
            answer = (long) Math.pow(root + 1, 2);
        }
        return answer;
    }
}
