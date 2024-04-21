package ps_traning.programmers.level_0;

public class 간단한_식_계산하기 {
    public int solution(String binomial) {
        int answer = 0;
        String[] binomialSplit = binomial.split(" ");
        int a = Integer.valueOf(binomialSplit[0]);
        String op = binomialSplit[1];
        int b = Integer.valueOf(binomialSplit[2]);
        if (op.equals("+")) {
            answer = a + b;
        } else if (op.equals("-")) {
            answer = a - b;
        } else if (op.equals("*")) {
            answer = a * b;
        }
        return answer;
    }
}
