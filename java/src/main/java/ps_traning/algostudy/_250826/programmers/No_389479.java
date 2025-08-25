package ps_traning.algostudy._250826.programmers;

import java.util.ArrayDeque;
import java.util.Queue;

class No_389479 {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        int n = players.length;

        Queue<Integer> q = new ArrayDeque<>();
        for (int i = 0; i < n; i++) {
            while (!q.isEmpty() && i - q.peek() >= k) q.poll();

            int p = q.size();
            if ((p + 1) * m - 1 < players[i]) {
                for (int j = 0; j < (players[i] - ((p + 1) * m)) / m; j++) {
                    q.offer(i);
                    answer++;
                }
                q.offer(i);
                answer++;
            }

        }
        return answer;
    }
}
