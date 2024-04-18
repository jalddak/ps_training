package ps_traning.programmers.level_0;

public class 가위_바위_보 {
    public String solution(String rsp) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        for (char c : rsp.toCharArray()) {
            if (c == '2') {
                sb.append('0');
            } else if (c == '0') {
                sb.append('5');
            } else if (c == '5') {
                sb.append('2');
            }
        }
        answer = sb.toString();
        return answer;
    }
}
