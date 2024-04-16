package ps_traning.programmers.level_0;

public class 머쓱이보다_키_큰_사람 {
    public int solution(int[] array, int height) {
        int answer = 0;
        for (int temp : array) {
            if (temp > height) {
                answer++;
            }
        }
        return answer;
    }
}
