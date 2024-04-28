package ps_traning.programmers.level_2;

import java.util.Stack;

public class 짝지어_제거하기 {
    public int solution(String s) {
        int answer = 0;
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (stack.size() == 0 || stack.peek() != c) {
                stack.push(c);
            } else {
                stack.pop();
            }
        }
        if (stack.size() == 0) {
            answer = 1;
        }
        return answer;
    }
}
