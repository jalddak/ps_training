package ps_traning.programmers.level_0;

public class rny_string {
    public String solution(String rny_string) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        for (char c : rny_string.toCharArray()) {
            if (c == 'm') {
                sb.append("rn");
            } else {
                sb.append(c);
            }
        }
        answer = sb.toString();
        return answer;
    }
}
