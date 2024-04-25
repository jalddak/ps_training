package ps_traning.programmers.level_2;

import java.util.Stack;

public class 올바른_괄호 {
    boolean solution(String s) {
        boolean answer = true;
        Stack stk = new Stack();
        for (char c : s.toCharArray()) {
            if (c == '(') {
                stk.push(1);
            } else if (c == ')') {
                if (stk.size() == 0) {
                    answer = false;
                    break;
                }
                stk.pop();
            }
        }
        if (stk.size() != 0) {
            answer = false;
        }

        return answer;
    }
}
