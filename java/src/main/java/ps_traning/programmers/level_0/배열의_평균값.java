package ps_traning.programmers.level_0;

public class 배열의_평균값 {
    public double solution(int[] numbers) {
        double answer = 0;
        for (int num : numbers) {
            answer += num;
        }
        answer /= numbers.length;
        return answer;
    }
}
