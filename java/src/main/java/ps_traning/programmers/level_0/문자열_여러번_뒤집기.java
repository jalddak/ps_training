package ps_traning.programmers.level_0;

public class 문자열_여러번_뒤집기 {
    public String solution(String my_string, int[][] queries) {
        String answer = "";
        StringBuilder sb = new StringBuilder(my_string);
        for (int[] query : queries) {
            StringBuilder sub = new StringBuilder(sb.substring(query[0], query[1] + 1));
            sub = sub.reverse();
            sb.replace(query[0], query[1] + 1, sub.toString());
        }
        answer = sb.toString();
        return answer;
    }
}
