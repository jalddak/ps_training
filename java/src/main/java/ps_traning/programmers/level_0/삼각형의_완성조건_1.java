package ps_traning.programmers.level_0;

import java.util.Arrays;

public class 삼각형의_완성조건_1 {
    public int solution(int[] sides) {
        Arrays.sort(sides);
        if (sides[0] + sides[1] <= sides[2]) {
            return 2;
        }
        return 1;
    }
}
