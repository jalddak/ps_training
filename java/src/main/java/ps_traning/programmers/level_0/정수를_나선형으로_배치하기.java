package ps_traning.programmers.level_0;

public class 정수를_나선형으로_배치하기 {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        int[] dy = {0, 1, 0, -1};
        int[] dx = {1, 0, -1, 0};
        int d = 0;
        int num = 1;
        int y = 0, x = 0;
        answer[y][x] = num++;
        while (num <= n * n) {
            while (true) {
                int ny = y + dy[d], nx = x + dx[d];
                if (ny < 0 || ny >= n) {
                    d = (d + 1 < 4) ? d + 1 : d + 1 - 4;
                    continue;
                }
                if (nx < 0 || nx >= n) {
                    d = (d + 1 < 4) ? d + 1 : d + 1 - 4;
                    continue;
                }
                if (answer[ny][nx] != 0) {
                    d = (d + 1 < 4) ? d + 1 : d + 1 - 4;
                    continue;
                }
                y = ny;
                x = nx;
                break;
            }
            answer[y][x] = num++;
        }
        return answer;
    }
}
