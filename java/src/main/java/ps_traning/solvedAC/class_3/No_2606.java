package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class No_2606 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int m = Integer.valueOf(br.readLine());

        List<Integer>[] g = new ArrayList[n + 1];

        for (int i = 0; i <= n; i++) {
            g[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.valueOf(st.nextToken());
            int b = Integer.valueOf(st.nextToken());
            g[a].add(b);
            g[b].add(a);
        }

        Set<Integer> set = new HashSet<>();
        Queue<Integer> q = new LinkedList<>();
        q.add(1);
        set.add(1);

        while (!q.isEmpty()) {
            int num = q.poll();
            for (int next : g[num]) {
                if (set.contains(next)) continue;
                q.offer(next);
                set.add(next);
            }
        }

        System.out.println(set.size() - 1);
    }
}
