package ps_traning.programmers.level_1;

public class 하사드_수 {
    public boolean solution(int x) {
        boolean answer = true;
        String strX = String.valueOf(x);
        int temp = 0;
        for (char c : strX.toCharArray()) {
            temp += c - '0';
        }
        if (x % temp != 0) {
            answer = false;
        }
        return answer;
    }
}
