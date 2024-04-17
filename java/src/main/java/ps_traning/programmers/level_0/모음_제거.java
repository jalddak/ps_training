package ps_traning.programmers.level_0;

public class 모음_제거 {
    public String solution(String my_string) {
        String[] ban = {"a", "e", "i", "o", "u"};
        for (String alphabet : ban) {
            my_string = my_string.replaceAll(alphabet, "");
        }
        return my_string;
    }
}
