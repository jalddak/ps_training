package ps_traning.programmers.level_0;

import java.util.ArrayList;
import java.util.List;

public class 배열의_원소만큼_추가하기 {
    public List<Integer> solution(int[] arr) {
        List<Integer> list = new ArrayList<>();
        for (int n : arr) {
            for (int i = 0; i < n; i++) {
                list.add(n);
            }
        }
        return list;
    }
}
