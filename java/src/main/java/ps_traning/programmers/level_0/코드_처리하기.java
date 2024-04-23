package ps_traning.programmers.level_0;

public class 코드_처리하기 {
    public String solution(String code) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        int mode = 0;
        for (int i = 0; i < code.length(); i++) {
            if (code.charAt(i) == '1') {
                mode = (mode == 0) ? 1 : 0;
                continue;
            }
            if (i % 2 == 0 && mode == 0) sb.append(code.charAt(i));
            if (i % 2 == 1 && mode == 1) sb.append(code.charAt(i));
        }
        if (sb.length() == 0) {
            sb.append("EMPTY");
        }
        answer = sb.toString();
        return answer;
    }
}
