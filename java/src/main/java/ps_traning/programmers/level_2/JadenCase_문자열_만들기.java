package ps_traning.programmers.level_2;

public class JadenCase_문자열_만들기 {
    public String solution(String s) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        boolean flag = true;
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) {
                sb.append(c);
                flag = false;
            } else if (c == ' ') {
                sb.append(c);
                flag = true;
            } else if (flag) {
                sb.append(Character.toUpperCase(c));
                flag = false;
            } else {
                sb.append(Character.toLowerCase(c));
            }
        }
        answer = sb.toString();
        return answer;
    }
}
