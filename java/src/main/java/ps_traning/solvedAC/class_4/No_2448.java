package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class No_2448 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());

        StringBuilder sb = new StringBuilder();
        List<String> result = recursion(n);
        for (int i = 0; i < result.size(); i++) {
            sb.append(result.get(i)).append("\n");
        }
        System.out.print(sb.toString());

    }

    private static List<String> recursion(int n) {
        if (n == 3) return new ArrayList<>(List.of("  *  ", " * * ", "*****"));
        int half = n / 2;
        List<String> result = recursion(half);
        String temp = "";
        for (int i = 0; i < half; i++) {
            temp += " ";
        }
        for (int i = 0; i < half; i++) {
            String row = result.get(i);
            result.add(row + " " + row);
            result.set(i, temp + row + temp);
        }
        return result;
    }
}
