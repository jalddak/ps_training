package ps_traning.programmers.level_0;

public class 배열_두배_만들기 {
    public int[] solution(int[] numbers) {
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] *= 2;
        }
        return numbers;
    }
}
