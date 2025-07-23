package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class No_2448 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());

        List<String> result = recursion(n);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(result.get(i)).append("\n");
        }
        System.out.print(sb);

    }

    private static List<String> recursion(int n) {
        List<String> result = new ArrayList<>();

        if (n == 3) {
            result.add("  *  ");
            result.add(" * * ");
            result.add("*****");
            return result;
        }

        int nn = n / 2;
        StringBuilder space = new StringBuilder();
        for (int i = 0; i < nn; i++) {
            space.append(" ");
        }
        List<String> small = recursion(nn);
        for (int i = 0; i < nn; i++) {
            result.add(space + small.get(i) + space);
        }

        for (int i = 0; i < nn; i++) {
            result.add(small.get(i) + " " + small.get(i));
        }
        return result;
    }
}

