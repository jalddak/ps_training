package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

// bfs
public class No_1389_bfs {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken());
        int m = Integer.valueOf(st.nextToken());
        List<List<Integer>> relations = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            relations.add(new ArrayList<>());
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int n1 = Integer.valueOf(st.nextToken());
            int n2 = Integer.valueOf(st.nextToken());

            relations.get(n1).add(n2);
            relations.get(n2).add(n1);
        }

        int answer = 0;
        int cnt = 10000;
        for (int i = 1; i <= n; i++) {
            int[] kbNum = new int[n + 1];
            Arrays.fill(kbNum, 101);
            kbNum[0] = 0;
            kbNum[i] = 0;
            Queue<int[]> q = new LinkedList<>(List.of(new int[]{i, 0}));
            while (!q.isEmpty()) {
                int[] nodeAndNum = q.poll();
                int node = nodeAndNum[0];
                int num = nodeAndNum[1];
                for (int f : relations.get(node)) {
                    if (num < kbNum[f]) {
                        kbNum[f] = num;
                        q.add(new int[]{f, num + 1});
                    }
                }
            }
            int temp = Arrays.stream(kbNum).sum();
            if (temp < cnt) {
                answer = i;
                cnt = temp;
            }
        }

        System.out.println(answer);

    }
}
