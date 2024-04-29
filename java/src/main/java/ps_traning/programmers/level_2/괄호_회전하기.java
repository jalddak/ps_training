package ps_traning.programmers.level_2;

import java.util.*;

public class 괄호_회전하기 {
    public boolean check(Queue<Character> queue) {
        Stack<Character> stack = new Stack<>();
        boolean result = true;
        Set<Character> set = new HashSet<>(Arrays.asList('{', '(', '['));
        List<Character> list = new ArrayList<>(queue);
        for (char c : list) {
            if (set.contains(c)) {
                stack.push(c);
            } else if (c == '}') {
                if (!stack.isEmpty() && stack.peek() == '{') {
                    stack.pop();
                } else {
                    result = false;
                    break;
                }
            } else if (c == ')') {
                if (!stack.isEmpty() && stack.peek() == '(') {
                    stack.pop();
                } else {
                    result = false;
                    break;
                }
            } else if (c == ']') {
                if (!stack.isEmpty() && stack.peek() == '[') {
                    stack.pop();
                } else {
                    result = false;
                    break;
                }
            }
        }

        if (!stack.isEmpty()) result = false;
        return result;
    }

    public int solution(String s) {
        int answer = 0;
        Queue<Character> queue = new LinkedList<>();
        for (Character c : s.toCharArray()) {
            queue.offer(c);
        }
        for (int i = 0; i < s.length(); i++) {
            if (check(queue)) answer++;
            queue.offer(queue.poll());
        }
        return answer;
    }
}
