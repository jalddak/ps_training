package ps_traning.programmers.level_1;

import java.util.Arrays;

public class 문자열_내림차순으로_배치하기 {
    public String solution(String s) {
        String answer = "";
        char[] arr = s.toCharArray();
        Arrays.sort(arr);
        StringBuilder sb = new StringBuilder(String.valueOf(arr));
        answer = sb.reverse().toString();
        return answer;
    }
}
