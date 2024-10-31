package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class No_10828 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        StringBuilder sb = new StringBuilder();
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String[] cmd = new String[2];
            int index = 0;
            while (st.hasMoreTokens()) cmd[index++] = st.nextToken();
            if (cmd[0].equals("push")) {
                stack.push(Integer.valueOf(cmd[1]));
            } else if (cmd[0].equals("pop")) {
                sb.append(!stack.empty() ? stack.pop() : -1).append("\n");
            } else if (cmd[0].equals("size")) {
                sb.append(stack.size()).append("\n");
            } else if (cmd[0].equals("empty")) {
                sb.append(!stack.empty() ? 0 : 1).append("\n");
            } else if (cmd[0].equals("top")) {
                sb.append(!stack.empty() ? stack.peek() : -1).append("\n");
            }
        }
        System.out.println(sb.toString());
    }
}
