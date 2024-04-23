package ps_traning.programmers.level_0;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class 전국_대회_선발_고사 {
    public int solution(int[] rank, boolean[] attendance) {
        int answer = 0;
        List<Integer> rankList = new ArrayList<>();
        for (int r : rank) {
            rankList.add(r);
        }
        List<Integer> candidate = new ArrayList<>();
        for (int i = 0; i < rank.length; i++) {
            if (attendance[i]) candidate.add(rank[i]);
        }
        Collections.sort(candidate);
        answer += rankList.indexOf(candidate.get(0)) * 10000
                + rankList.indexOf(candidate.get(1)) * 100
                + rankList.indexOf(candidate.get(2));
        return answer;
    }
}
