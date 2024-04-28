package ps_traning.programmers.level_1;

public class 최소직사각형 {
    public int solution(int[][] sizes) {
        int answer = 0;
        int bMax = 0;
        int sMax = 0;
        for (int[] size : sizes) {
            bMax = Math.max(bMax, Math.max(size[0], size[1]));
            sMax = Math.max(sMax, Math.min(size[0], size[1]));
        }
        answer = bMax * sMax;
        return answer;
    }
}
