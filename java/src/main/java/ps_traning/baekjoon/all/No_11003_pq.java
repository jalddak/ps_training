package ps_traning.baekjoon.all;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

// 시간초과
public class No_11003_pq {

    private static int n, l;
    private static int[] a;

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());

        a = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < l; i++) {
            pq.offer(a[i]);
            answer.add(pq.peek());
        }

        Map<Integer, Integer> map = new HashMap<>();
        for (int i = l; i < n; i++) {
            int out = a[i - l];
            map.put(out, map.containsKey(out) ? map.get(out) + 1 : 1);
            pq.offer(a[i]);

            int cMin = pq.peek();
            while (map.containsKey(cMin) && map.get(cMin) > 0) {
                pq.poll();
                map.put(cMin, map.get(cMin) - 1);
                cMin = pq.peek();
            }

            answer.add(cMin);
        }

        StringBuilder sb = new StringBuilder();
        for (int a : answer) {
            sb.append(a).append(" ");
        }
        System.out.println(sb);
    }
}