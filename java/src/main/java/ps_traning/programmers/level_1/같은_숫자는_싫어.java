package ps_traning.programmers.level_1;

import java.util.Stack;

public class 같은_숫자는_싫어 {
    public int[] solution(int[] arr) {
        Stack<Integer> stk = new Stack<>();
        stk.push(arr[0]);
        for (int i = 1; i < arr.length; i++) {
            if (stk.peek() != arr[i]) {
                stk.push(arr[i]);
            }
        }
        int[] answer = new int[stk.size()];
        for (int i = 0; i < stk.size(); i++) {
            answer[i] = stk.get(i);
        }

        return answer;
    }
}
