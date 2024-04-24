package ps_traning.programmers.level_1;

public class 나머지가_1이되는_수찾기 {
    public int solution(int n) {
        int answer = n - 1;
        for (int i = 2; i <= (int) Math.sqrt(n); i++) {
            if (answer % i == 0) {
                answer = i;
                break;
            }
        }
        return answer;
    }
}
