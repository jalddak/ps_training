package ps_traning.programmers.level_0;

public class 배열_비교하기 {
    public int sum(int[] arr) {
        int result = 0;
        for (int n : arr) {
            result += n;
        }
        return result;
    }

    public int solution(int[] arr1, int[] arr2) {
        int answer = 0;
        if (arr1.length > arr2.length ||
                (arr1.length == arr2.length && sum(arr1) > sum(arr2))) {
            answer = 1;
        } else if (arr1.length < arr2.length ||
                (arr1.length == arr2.length && sum(arr1) < sum(arr2))) {
            answer = -1;
        } else {
            answer = 0;
        }
        return answer;
    }
}
