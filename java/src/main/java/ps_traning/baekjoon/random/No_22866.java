package ps_traning.baekjoon.random;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class No_22866 {

    private static int[] hs;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        hs = new int[n];
        int[][] result = new int[n][2];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            hs[i] = Integer.valueOf(st.nextToken());
        }

        Deque<int[]> deque = new ArrayDeque<>();
        deque.push(new int[]{1, hs[0]});

        for (int i = 1; i < n; i++) {
            while (!deque.isEmpty()) {
                if (hs[i] >= deque.peekLast()[1]) deque.removeLast();
                else break;
            }
            if (!deque.isEmpty()) {
                result[i][0] += deque.size();
                result[i][1] = deque.peekLast()[0];
            }
            deque.addLast(new int[]{i + 1, hs[i]});
        }

        deque = new ArrayDeque<>();
        deque.offer(new int[]{n, hs[n - 1]});

        for (int i = n - 2; i >= 0; i--) {
            while (!deque.isEmpty()) {
                if (hs[i] >= deque.peekLast()[1]) deque.removeLast();
                else break;
            }
            if (!deque.isEmpty()) {
                result[i][0] += deque.size();
                
                if (result[i][1] == 0 ||
                        (Math.abs(result[i][1] - (i + 1)) > Math.abs(deque.peekLast()[0] - (i + 1)))) {
                    result[i][1] = deque.peekLast()[0];
                }
            }
            deque.addLast(new int[]{i + 1, hs[i]});
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            int cnt = result[i][0];
            sb.append(cnt).append(" ");
            if (cnt != 0) sb.append(result[i][1]);
            sb.append("\n");
        }

        System.out.print(sb);
    }

}

