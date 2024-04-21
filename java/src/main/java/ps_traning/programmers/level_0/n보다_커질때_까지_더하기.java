package ps_traning.programmers.level_0;

public class n보다_커질때_까지_더하기 {
    public int solution(int[] numbers, int n) {
        int answer = 0;
        int index = 0;
        while (answer <= n) {
            answer += numbers[index];
            index++;
        }
        return answer;
    }
}
