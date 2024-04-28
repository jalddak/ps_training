package ps_traning.programmers.level_2;

public class 점프와_순간_이동 {
    public int solution(int n) {
        int ans = 1;
        while (n != 1) {
            ans += n % 2;
            n /= 2;
        }

        return ans;
    }
}
