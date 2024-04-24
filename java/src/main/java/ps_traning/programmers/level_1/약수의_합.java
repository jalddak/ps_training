package ps_traning.programmers.level_1;

public class 약수의_합 {
    class Solution {
        public int solution(int n) {
            int answer = 0;
            for (int num = 1; num <= (int) Math.sqrt(n); num++) {
                if (n % num == 0) {
                    answer += num;
                    if (n / num != num) {
                        answer += n / num;
                    }
                }
            }
            return answer;
        }
    }
}
