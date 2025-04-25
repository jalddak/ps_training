package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_7662 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.valueOf(br.readLine());
        for (int i = 0; i < t; i++) {
            int k = Integer.valueOf(br.readLine());

            Map<Integer, Integer> map = new HashMap<>();
            PriorityQueue<Integer> minHeap = new PriorityQueue<>();
//            PriorityQueue<Integer> maxHeap = new PriorityQueue<>(new Comparator<Integer>() {
//                @Override
//                public int compare(Integer o1, Integer o2) {
//                    if (o2 - o1 > 0) return 1;
//                    else if (o2 - o1 == 0) return 0;
//                    else return -1;
//                }
//            });
            PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());

            for (int j = 0; j < k; j++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                String cmd = st.nextToken();
                int n = Integer.valueOf(st.nextToken());
                if (cmd.equals("I")) {
                    if (!map.containsKey(n)) map.put(n, 1);
                    else map.replace(n, map.get(n) + 1);
                    maxHeap.add(n);
                    minHeap.add(n);
                } else if (cmd.equals("D")) {
                    if (n == -1) {
                        deleteNum(minHeap, map);
                    } else if (n == 1) {
                        deleteNum(maxHeap, map);
                    }
                }
            }

            int maxN = searchNum(maxHeap, map);
            int minN = searchNum(minHeap, map);

            if (!maxHeap.isEmpty()) sb.append(maxN).append(" ").append(minN);
            else sb.append("EMPTY");
            sb.append("\n");
        }

        System.out.print(sb.toString());
    }

    private static int searchNum(PriorityQueue<Integer> heap, Map<Integer, Integer> map) {
        int n = 0;
        while (!heap.isEmpty()) {
            int temp = heap.peek();
            if (map.containsKey(temp) && map.get(temp) > 0) {
                n = temp;
                break;
            }
            heap.poll();
        }
        return n;
    }

    private static void deleteNum(PriorityQueue<Integer> heap, Map<Integer, Integer> map) {
        while (!heap.isEmpty()) {
            int delN = heap.poll();
            if (map.containsKey(delN) && map.get(delN) > 0) {
                map.replace(delN, map.get(delN) - 1);
                break;
            }
        }
    }
}
