package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_1918 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] ip = br.readLine().toCharArray();
        StringBuilder sb = new StringBuilder();

        Set<Character> expression = new HashSet<>(List.of('+', '-', '*', '/', '(', ')'));
        Map<Character, Integer> rank = new HashMap<>();
        rank.put('+', 1);
        rank.put('-', 1);
        rank.put('*', 2);
        rank.put('/', 2);
        Stack<Character> stack = new Stack<>();

        for (char a : ip) {
            if (!expression.contains(a)) {
                sb.append(a);
                continue;
            }
            if (a == ')') {
                while (stack.peek() != '(') sb.append(stack.pop());
                stack.pop();
                continue;
            }
            while (!stack.isEmpty() && a != '(' && stack.peek() != '(' && rank.get(stack.peek()) >= rank.get(a)) {
                sb.append(stack.pop());
            }
            stack.push(a);
        }
        while (!stack.isEmpty()) sb.append(stack.pop());
        System.out.println(sb.toString());
    }
}
