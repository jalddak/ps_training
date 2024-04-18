package ps_traning.programmers.level_0;

public class 개미_군단 {
    public int solution(int hp) {
        int answer = 0;
        answer += (int) hp / 5;
        hp = hp % 5;
        answer += (int) hp / 3;
        hp = hp % 3;
        answer += hp;
        return answer;
    }
}
