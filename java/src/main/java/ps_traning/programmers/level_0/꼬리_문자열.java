package ps_traning.programmers.level_0;

public class 꼬리_문자열 {
    public String solution(String[] str_list, String ex) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        for (String str : str_list) {
            if (str.contains(ex)) {
                continue;
            }
            sb.append(str);
        }
        answer = sb.toString();
        return answer;
    }
}
