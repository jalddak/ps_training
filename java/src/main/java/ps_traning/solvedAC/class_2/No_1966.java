package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class No_1966 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.valueOf(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] nm = new int[2];
            int index = 0;
            while (st.hasMoreTokens()) nm[index++] = Integer.valueOf(st.nextToken());
            Queue<Integer> q = new LinkedList<>();
            Stack<Integer> s = new Stack<>();
            st = new StringTokenizer(br.readLine());
            while (st.hasMoreTokens()) {
                int num = Integer.valueOf(st.nextToken());
                q.offer(num);
                s.push(num);
            }
            s.sort(Integer::compareTo);

            int cnt = 0;
            while (nm[1] >= 0) {
                int num = q.poll();
                nm[1] -= 1;
                if (num == s.peek()) {
                    s.pop();
                    cnt += 1;
                } else {
                    q.offer(num);
                    nm[1] = nm[1] == -1 ? q.size() - 1 : nm[1];
                }
            }
            sb.append(cnt + "\n");
        }
        System.out.println(sb.toString());
    }
}
