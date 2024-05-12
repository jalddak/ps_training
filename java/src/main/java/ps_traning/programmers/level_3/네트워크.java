package ps_traning.programmers.level_3;

import java.util.Stack;

public class 네트워크 {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (visited[i]) continue;
            answer++;
            Stack<Integer> st = new Stack<>();
            st.push(i);
            visited[i] = true;
            while (!st.isEmpty()) {
                int current = st.pop();
                for (int j = 0; j < n; j++) {
                    if (computers[current][j] == 1 && !visited[j]) {
                        visited[j] = true;
                        st.push(j);
                    }
                }
            }
        }
        return answer;
    }
}
