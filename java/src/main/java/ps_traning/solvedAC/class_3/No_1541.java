package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class No_1541 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] arr = br.readLine().split("-");
        int answer = Arrays.stream(arr[0].split("\\+")).mapToInt(Integer::parseInt).sum();
        for (int i = 1; i < arr.length; i++) {
            String calc = arr[i];
            answer -= Arrays.stream(calc.split("\\+")).mapToInt(Integer::parseInt).sum();
        }
        System.out.println(answer);

    }
}
