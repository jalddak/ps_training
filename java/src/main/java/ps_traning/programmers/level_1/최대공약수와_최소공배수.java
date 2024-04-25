package ps_traning.programmers.level_1;

public class 최대공약수와_최소공배수 {
    public int[] solution(int n, int m) {
        int gcd = 1;
        for (int num = 2; num <= Math.min(n, m); num++) {
            if (n % num == 0 && m % num == 0) {
                gcd = num;
            }
        }

        int lcm = gcd * (n / gcd) * (m / gcd);
        int[] answer = {gcd, lcm};
        return answer;
    }
}
