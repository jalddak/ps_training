package ps_traning.programmers.level_1;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


/**
 * Map value 기준으로 정렬하는 방법
 * 자바 람다식 이용 (Map 에서 get 해서 얻은 Double을 - 로 비교하려니 오류나서 compareTo 이용함)
 * double 타입은 - 로 비교 안됨.
 */
public class _0V_실패율 {
    public List<Integer> solution(int N, int[] stages) {
        Map<Integer, Integer> fail = new HashMap<>();
        Map<Integer, Double> info = new HashMap<>();
        int users = stages.length;

        for (int n = 1; n <= N; n++) {
            fail.put(n, 0);
            info.put(n, 0.0);
        }
        for (int s : stages) {
            if (s > N) continue;
            fail.replace(s, fail.get(s) + 1);
        }

        for (int n = 1; n <= N; n++) {
            info.replace(n, (double) fail.get(n) / users);
            users = users - fail.get(n);
            if (users == 0) break;
        }

        List<Integer> answer = new ArrayList<>(info.keySet());
        answer.sort((o1, o2) -> info.get(o2).compareTo(info.get(o1)));

        return answer;
    }
}
