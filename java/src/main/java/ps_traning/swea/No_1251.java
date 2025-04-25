package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class No_1251 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("#").append(tc).append(" ");
            int n = Integer.valueOf(br.readLine());
            int[] ys = new int[n];
            int[] xs = new int[n];

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                xs[i] = Integer.valueOf(st.nextToken());
            }
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                ys[i] = Integer.valueOf(st.nextToken());
            }

            List<Object>[] info = new List[n];
            for (int i = 0; i < n; i++) {
                info[i] = new ArrayList<>();
            }
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    double l = calcDistance(ys[i], xs[i], ys[j], xs[j]);

                    List<Object> pair1 = new ArrayList<>();
                    pair1.add(l);
                    pair1.add(j);
                    info[i].add(pair1);

                    List<Object> pair2 = new ArrayList<>();
                    pair2.add(l);
                    pair2.add(i);
                    info[j].add(pair2);

                    info[i].add(pair1);
                    info[j].add(pair2);
                }
            }
            double e = Double.valueOf(br.readLine());

            PriorityQueue<Object[]> pq = new PriorityQueue<>(
                    (o1, o2) -> ((Double) o1[0]).compareTo((Double) o2[0])
            );
            pq.offer(new Object[]{0.0, 0});
            boolean[] visited = new boolean[n];

            double doubleResult = 0;
            while (!pq.isEmpty()) {
                Object[] cur = pq.poll();
                double l = (Double) cur[0];
                int loca = (Integer) cur[1];
                if (visited[loca]) continue;
                visited[loca] = true;
                doubleResult += e * (Math.pow(l, 2));

                for (Object o : info[loca]) {
                    List<Object> next = (List<Object>) o;
                    pq.offer(new Object[]{next.get(0), next.get(1)});
                }
            }

            long result = Math.round(doubleResult);
            sb.append(result).append("\n");
        }
        System.out.print(sb);
    }

    public static double calcDistance(int ay, int ax, int by, int bx) {
        return Math.sqrt(Math.pow(ay - by, 2) + Math.pow(ax - bx, 2));
    }
}
