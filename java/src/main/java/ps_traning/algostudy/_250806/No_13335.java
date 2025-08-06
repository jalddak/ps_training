package ps_traning.algostudy._250806;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class No_13335 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());

        Queue<Integer> ts = new ArrayDeque<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            ts.offer(Integer.parseInt(st.nextToken()));
        }

        int curL = 0;
        int t = 0;
        Queue<int[]> q = new ArrayDeque<>();
        while (!q.isEmpty() || !ts.isEmpty()) {
            if (!q.isEmpty()) {
                if (q.peek()[1] == w) {
                    curL -= q.poll()[0];
                }
                for (int i = 0; i < q.size(); i++) {
                    int[] poll = q.poll();
                    poll[1] += 1;
                    q.offer(poll);
                }
            }
            if (!ts.isEmpty() && l >= curL + ts.peek()) {
                int temp = ts.poll();
                q.offer(new int[]{temp, 1});
                curL += temp;
            }
            t++;
        }

        System.out.println(t);
    }
}