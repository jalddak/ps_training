package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_1238 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = 10;
        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("#").append(tc).append(" ");
            StringTokenizer st = new StringTokenizer(br.readLine());
            int len = Integer.parseInt(st.nextToken());
            int start = Integer.parseInt(st.nextToken());

            st = new StringTokenizer(br.readLine());
            Map<Integer, List<Integer>> map = new HashMap<>();
            for (int i = 0; i < len; i += 2) {
                int f = Integer.parseInt(st.nextToken());
                int t = Integer.parseInt(st.nextToken());

                if (!map.containsKey(f)) {
                    map.put(f, new ArrayList<>());
                }
                map.get(f).add(t);
            }

            Queue<int[]> queue = new LinkedList<>();
            queue.offer(new int[]{start, 0});

            Set<Integer> visited = new HashSet<>();
            visited.add(start);
            List<Integer> candidates = new ArrayList<>();

            int maxW = -1;
            while (!queue.isEmpty()) {
                int[] cur = queue.poll();
                int x = cur[0];
                int w = cur[1];
                if (maxW < w) {
                    maxW = w;
                    candidates.clear();
                }
                candidates.add(cur[0]);

                if (!map.containsKey(x)) continue;
                for (int nx : map.get(x)) {
                    if (visited.contains(nx)) continue;
                    queue.offer(new int[]{nx, w + 1});
                    visited.add(nx);
                }
            }

            Integer result = candidates.stream().max(Integer::compareTo).get();
            sb.append(result).append("\n");
        }
        System.out.print(sb);
    }
}
