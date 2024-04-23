package ps_traning.programmers.level_0;

public class 문자_개수_세기 {
    public int[] solution(String my_string) {
        int[] answer = new int[52];
        for (char c : my_string.toCharArray()) {
            if (Character.isUpperCase(c)) {
                answer[c - 'A'] += 1;
            } else {
                answer[c - 'a' + 26] += 1;
            }
        }
        return answer;
    }
}
