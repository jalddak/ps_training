package ps_traning.programmers.level_1;

import java.util.Arrays;

/**
 * comparator 사용
 * 람다식 사용
 */
public class _0V_문자열_내_마음대로_정렬하기 {
    public String[] solution(String[] strings, int n) {
        Arrays.sort(strings);
        Arrays.sort(strings, (s1, s2) -> s1.charAt(n) - s2.charAt(n));
        return strings;
    }
}
