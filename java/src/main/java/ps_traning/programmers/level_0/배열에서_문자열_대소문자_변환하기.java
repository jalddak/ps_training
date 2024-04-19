package ps_traning.programmers.level_0;

public class 배열에서_문자열_대소문자_변환하기 {
    public String[] solution(String[] strArr) {
        String[] answer = {};
        for (int i = 0; i < strArr.length; i++) {
            if (i % 2 != 0) {
                strArr[i] = strArr[i].toUpperCase();
            } else {
                strArr[i] = strArr[i].toLowerCase();
            }
        }
        answer = strArr;
        return answer;
    }
}
