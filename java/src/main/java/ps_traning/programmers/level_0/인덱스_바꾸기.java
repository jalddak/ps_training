package ps_traning.programmers.level_0;

public class 인덱스_바꾸기 {
    public String solution(String my_string, int num1, int num2) {
        String answer = "";
        char first = my_string.charAt(num1);
        char second = my_string.charAt(num2);
        char[] temp = my_string.toCharArray();
        temp[num1] = second;
        temp[num2] = first;
        answer = String.valueOf(temp);
        return answer;
    }
}
