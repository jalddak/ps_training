package ps_traning.programmers.level_1;

public class 이상한_문자_만들기 {
    class Solution {
        public String solution(String s) {
            String answer = "";
            StringBuilder sb = new StringBuilder();
            int flag = 1;
            for (int i = 0; i < s.length(); i++) {
                char c = s.charAt(i);
                if (c == ' ') {
                    flag = 1;
                } else if (flag == 1) {
                    c = Character.toUpperCase(c);
                    flag = 0;
                } else {
                    c = Character.toLowerCase(c);
                    flag = 1;
                }
                sb.append(c);
            }
            answer = sb.toString();
            return answer;
        }
    }
}
