package ps_traning.programmers.level_0;

public class 글자_이어_붙여_문자열_만들기 {
    public String solution(String my_string, int[] index_list) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        for (int index : index_list) {
            sb.append(my_string.charAt(index));
        }
        answer = sb.toString();
        return answer;
    }
}
