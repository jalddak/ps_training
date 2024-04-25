package ps_traning.programmers.level_1;

public class 약수의_개수와_덧셈 {
    public int solution(int left, int right) {
        int answer = 0;
        for (int n = left; n <= right; n++) {
            int cnt = 0;
            for (int s = 1; s <= (int) Math.sqrt(n); s++) {
                if (n % s != 0) {
                    continue;
                }
                cnt += 1;
                if (n / s != s) {
                    cnt += 1;
                }
            }
            if (cnt % 2 == 0) {
                answer += n;
            } else {
                answer -= n;
            }
        }
        return answer;
    }
}
