package ps_traning.programmers.level_2;

public class 피로도 {
    public int recursion(int k, int[][] dungeons, boolean[] visited, int depth, int result) {
        for (int i = 0; i < dungeons.length; i++) {
            if (visited[i]) continue;
            int need = dungeons[i][0], use = dungeons[i][1];
            if (k < need) continue;
            k -= use;
            visited[i] = true;
            result = Math.max(result, recursion(k, dungeons, visited, depth + 1, depth + 1));
            visited[i] = false;
            k += use;
        }
        return result;
    }

    public int solution(int k, int[][] dungeons) {
        int answer = 0;
        boolean[] visited = new boolean[dungeons.length];
        answer = recursion(k, dungeons, visited, 0, answer);
        return answer;
    }
}
