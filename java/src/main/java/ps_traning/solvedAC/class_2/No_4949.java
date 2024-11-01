package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.Stack;

public class No_4949 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        Set<Character> start = new HashSet<>(List.of('(', '['));
        Set<Character> end = new HashSet<>(List.of(')', ']'));
        while (true) {
            String str = br.readLine();
            Stack<Character> stack = new Stack<>();
            if (str.equals(".")) break;
            boolean flag = true;
            for (char c : str.toCharArray()) {
                if (start.contains(c)) stack.push(c);
                else if (end.contains(c)) {
                    if (c == ')' && (!stack.isEmpty() && stack.peek() == '(')) stack.pop();
                    else if (c == ']' && (!stack.isEmpty() && stack.peek() == '[')) stack.pop();
                    else {
                        flag = false;
                        break;
                    }
                }
            }
            if (!stack.isEmpty()) flag = false;
            if (flag) sb.append("yes\n");
            else sb.append("no\n");
        }
        System.out.println(sb.toString());
    }
}
