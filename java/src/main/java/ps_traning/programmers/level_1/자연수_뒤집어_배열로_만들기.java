package ps_traning.programmers.level_1;

public class 자연수_뒤집어_배열로_만들기 {
    public int[] solution(long n) {
        String strN = String.valueOf(n);
        int[] answer = new int[strN.length()];
        int index = strN.length() - 1;
        for (char c : strN.toCharArray()) {
            answer[index--] = c - '0';
        }
        return answer;
    }
}
