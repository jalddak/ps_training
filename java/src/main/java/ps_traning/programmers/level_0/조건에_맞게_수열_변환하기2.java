package ps_traning.programmers.level_0;

public class 조건에_맞게_수열_변환하기2 {
    public int solution(int[] arr) {
        int answer = 0;
        boolean check = false;
        while (!check) {
            check = true;
            for (int i = 0; i < arr.length; i++) {
                if (arr[i] >= 50 && arr[i] % 2 == 0) {
                    arr[i] /= 2;
                    check = false;
                } else if (arr[i] < 50 && arr[i] % 2 == 1) {
                    arr[i] = arr[i] * 2 + 1;
                    check = false;
                }
            }
            answer++;
        }
        return answer - 1;
    }

}
