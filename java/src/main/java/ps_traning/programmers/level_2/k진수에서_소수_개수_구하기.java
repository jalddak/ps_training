package ps_traning.programmers.level_2;

public class k진수에서_소수_개수_구하기 {
    public int solution(int n, int k) {
        int answer = 0;
        String[] nums = Integer.toString(n, k).split("0");
        Loop:
        for (String strNum : nums) {
            if (strNum.length() == 0) continue;
            long num = Long.valueOf(strNum);
            if (num <= 1) continue;
            for (long i = 2; i <= Math.sqrt(num); i++) {
                if (num % i == 0) {
                    continue Loop;
                }
            }
            answer++;
        }
        return answer;
    }
}
