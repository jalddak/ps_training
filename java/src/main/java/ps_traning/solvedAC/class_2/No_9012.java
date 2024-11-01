package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class No_9012 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            String cmd = br.readLine();
            Stack<Integer> stack = new Stack<>();
            boolean flag = true;
            for (char c : cmd.toCharArray()) {
                if (c == '(') stack.push(0);
                else if (!stack.isEmpty()) stack.pop();
                else flag = false;
            }
            if (!stack.isEmpty()) flag = false;
            if (flag) sb.append("YES\n");
            else sb.append("NO\n");
        }
        System.out.print(sb.toString());
    }
}
