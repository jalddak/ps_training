package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_1218 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        Map<Character, Character> pair = new HashMap<>();
        pair.put(']', '[');
        pair.put('}', '{');
        pair.put('>', '<');
        pair.put(')', '(');
        Set<Character> left = new HashSet<>(pair.values());
        Set<Character> right = pair.keySet();

        for (int tc = 1; tc <= 10; tc++) {
            sb.append("#").append(tc).append(" ");
            int len = Integer.valueOf(br.readLine());

            Stack<Character> stack = new Stack<>();
            int result = 1;

            char[] input = br.readLine().toCharArray();
            for (int i = 0; i < len; i++) {
                if (left.contains(input[i])) stack.push(input[i]);
                else if (right.contains(input[i])) {
                    if (stack.peek() == pair.get(input[i])) stack.pop();
                    else {
                        result = 0;
                        break;
                    }
                }
            }

            sb.append(result).append("\n");
        }
        System.out.print(sb);
    }
}
