package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_9935 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        String boom = br.readLine();
        int boomSize = boom.length();

        StringBuilder stack = new StringBuilder();
        for (char a : str.toCharArray()) {
            stack.append(a);
            int stackSize = stack.length();
            if (stack.length() < boomSize || stack.charAt(stackSize - 1) != boom.charAt(boomSize - 1)) continue;
            if (String.join("", stack.substring(stackSize - boomSize, stackSize)).equals(boom)) {
                for (int i = 0; i < boomSize; i++) {
                    stack.deleteCharAt(stackSize - 1 - i);
                }
            }
        }

        String answer = "FRULA";
//        if (!stack.isEmpty()) { << 왜 컴파일 에러인지는 모르겠음
        if (stack.length() != 0) {
            answer = stack.toString();
        }
        System.out.println(answer);
    }
}
