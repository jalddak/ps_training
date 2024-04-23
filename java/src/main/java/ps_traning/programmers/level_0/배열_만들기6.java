package ps_traning.programmers.level_0;

import java.util.Stack;

public class 배열_만들기6 {
    public Stack<Integer> solution(int[] arr) {
        Stack<Integer> answer = new Stack<>();
        for (int i = 0; i < arr.length; i++) {
            if (answer.size() == 0) {
                answer.push(arr[i]);
            } else if (answer.peek() == arr[i]) {
                answer.pop();
            } else {
                answer.push(arr[i]);
            }
        }
        if (answer.size() == 0) {
            answer.push(-1);
        }
        return answer;
    }
}
