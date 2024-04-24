package ps_traning.programmers.level_1;

public class 평균_구하기 {
    public double solution(int[] arr) {
        double answer = 0;
        for (int n : arr) {
            answer += n;
        }
        answer /= arr.length;
        return answer;
    }
}
