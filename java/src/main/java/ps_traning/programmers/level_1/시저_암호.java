package ps_traning.programmers.level_1;

public class 시저_암호 {
    public String solution(String s, int n) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (c == ' ') {
                c = c;
            } else if (Character.isUpperCase(c)) {
                c = (char) (c + n);
                if (c > 'Z') {
                    c = (char) (c - 'Z' + 'A' - 1);
                }
            } else {
                c = (char) (c + n);
                if (c > 'z') {
                    c = (char) (c - 'z' + 'a' - 1);
                }
            }
            sb.append(c);
        }
        answer = sb.toString();
        return answer;
    }
}
