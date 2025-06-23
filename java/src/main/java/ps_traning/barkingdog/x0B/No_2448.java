package ps_traning.barkingdog.x0B;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class No_2448 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());

        List<String> answer = rc(n);
        StringBuilder sb = new StringBuilder();
        for (String row : answer) {
            sb.append(row).append("\n");
        }
        System.out.print(sb);
    }

    private static List<String> rc(int n) {
        List<String> result = new ArrayList<>();
        if (n == 3) {
            result.add("  *  ");
            result.add(" * * ");
            result.add("*****");
            return result;
        }

        int nn = n / 2;
        List<String> before = rc(nn);
        for (String row : before) {
            result.add(" ".repeat(nn) + row + " ".repeat(nn));
        }

        for (String row : before) {
            result.add(row + " " + row);
        }

        return result;
    }
}
