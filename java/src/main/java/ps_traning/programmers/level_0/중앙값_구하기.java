package ps_traning.programmers.level_0;

import java.util.Arrays;

public class 중앙값_구하기 {
    class Solution {
        public int solution(int[] array) {
            Arrays.sort(array);
            return array[array.length / 2];
        }
    }
}
