package ps_traning.programmers.level_1;

public class 문자열_내의_p와_y의_개수 {
    boolean solution(String s) {
        boolean answer = true;
        int temp = 0;
        s = s.toLowerCase();
        for (char c : s.toCharArray()) {
            if (c == 'p') {
                temp += 1;
            } else if (c == 'y') {
                temp -= 1;
            }
        }
        if (temp != 0) {
            answer = false;
        }

        return answer;
    }
}
