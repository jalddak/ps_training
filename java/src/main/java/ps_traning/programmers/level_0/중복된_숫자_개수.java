package ps_traning.programmers.level_0;

public class 중복된_숫자_개수 {
    public int solution(int[] array, int n) {
        int answer = 0;
        for (int num : array) {
            if (num == n) {
                answer += 1;
            }
        }
        return answer;
    }
}
