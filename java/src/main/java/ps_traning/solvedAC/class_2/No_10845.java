package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class No_10845 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        StringBuilder sb = new StringBuilder();
        Queue<Integer> q = new LinkedList<>();
        int num = -1;
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String[] cmds = new String[2];
            int j = 0;
            while (st.hasMoreTokens()) cmds[j++] = st.nextToken();
            String cmd = cmds[0];
            if (cmd.equals("push")) {
                num = Integer.valueOf(cmds[1]);
                q.add(num);
            } else if (cmd.equals("pop")) {
                sb.append(!q.isEmpty() ? q.poll() : -1).append("\n");
            } else if (cmd.equals("size")) {
                sb.append(q.size()).append("\n");
            } else if (cmd.equals("empty")) {
                sb.append(q.isEmpty() ? 1 : 0).append("\n");
            } else if (cmd.equals("front")) {
                sb.append(!q.isEmpty() ? q.peek() : -1).append("\n");
            } else if (cmd.equals("back")) {
                sb.append(!q.isEmpty() ? num : -1).append("\n");
            }
        }
        System.out.println(sb.toString());

    }
}
