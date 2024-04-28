package ps_traning.programmers.level_1;

public class 숫자문자열과_영단어 {
    public int solution(String s) {
        int answer = 0;
        String[] strArr = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        String[] numArr = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};

        for (int i = 0; i <= 9; i++) {
            s = s.replaceAll(strArr[i], numArr[i]);
        }
        answer = Integer.valueOf(s);
        return answer;
    }
}
