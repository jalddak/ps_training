package ps_traning.programmers.level_0;

import java.util.List;
import java.util.Stack;

public class 배열_만들기4 {
    public List<Integer> solution(int[] arr) {
        Stack<Integer> stk = new Stack<>();
        for (int i = 0; i < arr.length; i++) {
            if (stk.size() == 0) {
                stk.push(arr[i]);
            } else if (stk.peek() < arr[i]) {
                stk.push(arr[i]);
            } else {
                stk.pop();
                i--;
            }
        }
        return stk;
    }
}
