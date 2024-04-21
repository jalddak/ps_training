package ps_traning.programmers.level_0;

import java.util.Stack;

public class 빈_배열에_추가_삭제하기 {
    public Stack<Integer> solution(int[] arr, boolean[] flag) {
        Stack<Integer> answer = new Stack<>();
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i]; j++) {
                if (flag[i]) {
                    answer.push(arr[i]);
                    answer.push(arr[i]);
                } else answer.pop();
            }
        }
        return answer;
    }
}
