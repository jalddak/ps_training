package ps_traning.programmers.level_0;

public class 옷가게_할인_받기 {
    public int solution(int price) {
        int answer = price;
        if (price >= 500000) {
            answer = (int) (price - price * 0.2);
        } else if (price >= 300000) {
            answer = (int) (price - price * 0.1);
        } else if (price >= 100000) {
            answer = (int) (price - price * 0.05);
        }
        return answer;
    }
}
