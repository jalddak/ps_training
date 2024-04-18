package ps_traning.programmers.level_0;

public class 양꼬치 {
    public int solution(int n, int k) {
        int answer = 12000 * n + 2000 * (k - (int) (n / 10));
        return answer;
    }
}
