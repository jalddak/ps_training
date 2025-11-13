package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class No_5430 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int tc = 0; tc < t; tc++) {
            String p = br.readLine();
            int n = Integer.parseInt(br.readLine());
            String input = br.readLine();
            String sArr = input.substring(1, input.length() - 1);
            StringTokenizer st = new StringTokenizer(sArr, ",");
            Deque<Integer> dq = new ArrayDeque<>();
            for (int i = 0; i < n; i++) {
                dq.add(Integer.parseInt(st.nextToken()));
            }

            boolean drt = true;
            boolean error = false;
            for (char cmd : p.toCharArray()) {
                if (cmd == 'D' && dq.isEmpty()) {
                    error = true;
                    break;
                }
                if (cmd == 'R') drt = !drt;
                else if (cmd == 'D') {
                    if (drt) dq.pollFirst();
                    else dq.pollLast();
                }
            }

            if (error) sb.append("error");
            else {
                sb.append("[");
                while (!dq.isEmpty()) {
                    if (drt) sb.append(dq.pollFirst());
                    else sb.append(dq.pollLast());
                    if (!dq.isEmpty()) sb.append(",");
                }
                sb.append("]");
            }
            sb.append("\n");
        }
        System.out.print(sb);

    }
}
