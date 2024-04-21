package ps_traning.programmers.level_0;

public class 문자열_섞기 {
    public String solution(String str1, String str2) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < str1.length(); i++) {
            sb.append(str1.charAt(i));
            sb.append(str2.charAt(i));
        }
        answer = sb.toString();
        return answer;
    }
}
