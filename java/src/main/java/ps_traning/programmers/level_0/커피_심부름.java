package ps_traning.programmers.level_0;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class 커피_심부름 {
    public int solution(String[] order) {
        int answer = 0;
        Set<String> americano = new HashSet<>(Arrays.asList(
                "iceamericano", "americanoice", "hotamericano", "americanohot"
                , "americano", "anything"));
        Set<String> cafelatte = new HashSet<>(Arrays.asList(
                "icecafelatte", "cafelatteice", "hotcafelatte", "cafelattehot", "cafelatte"
        ));

        for (String coffee : order) {
            if (americano.contains(coffee)) {
                answer += 4500;
            }
            if (cafelatte.contains(coffee)) {
                answer += 5000;
            }
        }
        return answer;
    }
}
