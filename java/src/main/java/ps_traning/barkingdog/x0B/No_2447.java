package ps_traning.barkingdog.x0B;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class No_2447 {
    private static int n;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.valueOf(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (String row : rc(n)) {
            sb.append(row.toString()).append("\n");
        }
        System.out.print(sb);
    }

    private static List<String> rc(int l) {
        if (l == 1) return new ArrayList<>(List.of("*"));

        int nl = l / 3;
        List<String> frag = rc(nl);
        List<String> result = new ArrayList<>();
        for (String row : frag) {
            result.add(row.repeat(3));
        }
        for (String row : frag) {
            result.add(row + " ".repeat(nl) + row);
        }
        for (String row : frag) {
            result.add(row.repeat(3));
        }
        return result;
    }

}
