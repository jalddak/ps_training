package ps_traning.programmers.level_0;

public class 몫_구하기 {

    public static void main(String[] args) {
        몫_구하기 s = new 몫_구하기();
        System.out.println(s.solution(11, 2));
    }

    public int solution(int num1, int num2) {
        int answer = num1 / num2;
        return answer;
    }
}
