package ps_traning.programmers.level_0;

public class l로_만들기 {
    public String solution(String myString) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        for (char c : myString.toCharArray()) {
            if (c < 'l') {
                sb.append('l');
            } else {
                sb.append(c);
            }
        }
        answer = sb.toString();
        return answer;
    }
}
