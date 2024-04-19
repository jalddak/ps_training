package ps_traning.programmers.level_0;

public class A_강조하기 {
    public String solution(String my_string) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        for (String str : my_string.split("")) {
            if (str.toLowerCase().equals("a")) {
                sb.append("A");
            } else {
                sb.append(str.toLowerCase());
            }
        }
        answer = sb.toString();
        return answer;
    }
}
