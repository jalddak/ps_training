package ps_traning.programmers.level_2;

public class N개의_최소공배수 {
    public int calc(int n1, int n2) {
        int gcd = 1;
        int minN = Math.min(n1, n2);
        for (int n = 2; n <= minN; n++) {
            if (n1 % n == 0 && n2 % n == 0) {
                gcd = n;
            }
        }
        return gcd * n1 / gcd * n2 / gcd;
    }

    public int solution(int[] arr) {
        if (arr.length == 1) {
            return arr[0];
        }
        int answer = calc(arr[0], arr[1]);
        for (int i = 2; i < arr.length; i++) {
            answer = calc(answer, arr[i]);
        }
        return answer;
    }
}
