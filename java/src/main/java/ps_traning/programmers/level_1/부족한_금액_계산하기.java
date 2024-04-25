package ps_traning.programmers.level_1;

public class 부족한_금액_계산하기 {
    public long solution(int price, int money, int count) {
        long answer = 0;
        long need = 0;
        for (int i = 1; i <= count; i++) {
            need += price * i;
        }
        if (need > money) {
            answer = need - money;
        }

        return answer;
    }
}
