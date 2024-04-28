package ps_traning.programmers.level_1;

public class _1차_비밀지도 {
    public String makeBinary(int num, int n) {
        StringBuilder sb = new StringBuilder(Integer.toString(num, 2));
        sb = sb.reverse();
        int len = sb.length();
        for (int i = 0; i < n - len; i++) {
            sb.append("0");
        }
        sb = sb.reverse();
        return sb.toString();
    }

    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        for (int i = 0; i < n; i++) {
            String b1 = makeBinary(arr1[i], n);
            String b2 = makeBinary(arr2[i], n);
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < n; j++) {
                if (b1.charAt(j) == '1' || b2.charAt(j) == '1') {
                    sb.append("#");
                } else {
                    sb.append(" ");
                }
            }
            answer[i] = sb.toString();
        }
        return answer;
    }
}
