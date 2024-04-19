package ps_traning.programmers.level_0;

public class 특정한_문자를_대문자로_바꾸기 {
    public String solution(String my_string, String alp) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        for (String str : my_string.split("")) {
            if (str.equals(alp)) {
                sb.append(alp.toUpperCase());
            } else {
                sb.append(str);
            }
        }
        answer = sb.toString();
        return answer;
    }
}
