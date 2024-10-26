package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class No_1874 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < n; i++) {
            q.offer(Integer.valueOf(br.readLine()));
        }
        Stack<Integer> s = new Stack<>();
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            s.push(i);
            sb.append("+\n");
            while (!s.isEmpty() && s.peek().equals(q.peek())) {
                sb.append("-\n");
                s.pop();
                q.poll();
            }
            if (!s.isEmpty() && s.peek() > q.peek()) {
                System.out.println("NO");
                System.exit(0);
            }
        }
        System.out.print(sb.toString());
    }
}
