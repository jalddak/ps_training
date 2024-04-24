package ps_traning.programmers.level_1;

public class 자릿수_더하기 {
    public class Solution {
        public int solution(int n) {
            int answer = 0;
            String strN = String.valueOf(n);
            for (char c : strN.toCharArray()) {
                answer += c - '0';
            }
            return answer;
        }
    }
}
