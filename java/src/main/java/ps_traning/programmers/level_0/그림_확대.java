package ps_traning.programmers.level_0;

public class 그림_확대 {
    public String[] solution(String[] picture, int k) {
        String[] answer = new String[picture.length * k];
        for (int i = 0; i < picture.length; i++) {
            String str = picture[i];
            StringBuilder sb = new StringBuilder();
            for (char c : str.toCharArray()) {
                for (int j = 0; j < k; j++) {
                    sb.append(c);
                }
            }
            for (int j = 0; j < k; j++) {
                answer[i * k + j] = sb.toString();
            }
        }
        return answer;
    }
}
