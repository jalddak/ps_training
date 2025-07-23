package ps_traning.s14.baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class No_10993 {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());

        List<StringBuilder> result = recursion(n);
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.size(); i++) {
            StringBuilder row = result.get(i);
            int index = row.length() - 1;
            int limit = 0;
            while (row.charAt(index--) == ' ') limit += 1;

            row.setLength(row.length() - limit);
            sb.append(row);
            if (i != result.size() - 1) sb.append("\n");
        }
        System.out.print(sb);

    }

    private static List<StringBuilder> recursion(int n) {
        List<StringBuilder> result = new ArrayList<>();

        if (n == 1) {
            result.add(new StringBuilder("*"));
            return result;
        }

        List<StringBuilder> before = recursion(n - 1);
        List<StringBuilder> small = before;
        if (n % 2 != 0) small = reverse(before);

        int bLLen = before.get(0).length();
        int bSLen = before.size();
        int sLen = bSLen * 2 + 1;
        int lLen = sLen * 2 - 1;

        StringBuilder stars = new StringBuilder();
        for (int i = 0; i < lLen; i++) {
            stars.append("*");
        }
        result.add(stars);

        for (int i = 0; i < bSLen; i++) {
            StringBuilder row = new StringBuilder();
            for (int j = 0; j <= i; j++) row.append(" ");
            row.append("*");
            for (int j = 0; j < (lLen - bLLen) / 2 - (i + 2); j++) row.append(" ");
            row.append(small.get(i));
            for (int j = 0; j < (lLen - bLLen) / 2 - (i + 2); j++) row.append(" ");
            row.append("*");
            for (int j = 0; j <= i; j++) row.append(" ");
            result.add(row);
        }

        for (int i = 0; i < bSLen - 1; i++) {
            StringBuilder row = new StringBuilder();
            for (int j = 0; j < bSLen; j++) row.append(" ");
            for (int j = 0; j <= i; j++) row.append(" ");
            row.append("*");
            for (int j = 0; j < (sLen - 1) - (2 + bSLen + i); j++) row.append(" ");
            row.append(" ");
            for (int j = 0; j < (sLen - 1) - (2 + bSLen + i); j++) row.append(" ");
            row.append("*");
            for (int j = 0; j <= i; j++) row.append(" ");
            for (int j = 0; j < bSLen; j++) row.append(" ");
            result.add(row);
        }

        StringBuilder last = new StringBuilder();
        for (int i = 0; i < sLen - 1; i++) last.append(" ");
        last.append("*");
        for (int i = 0; i < sLen - 1; i++) last.append(" ");
        result.add(last);


        if (n % 2 != 0) result = reverse(result);
        return result;
    }

    private static List<StringBuilder> reverse(List<StringBuilder> ori) {
        List<StringBuilder> result = new ArrayList<>();
        for (int i = ori.size() - 1; i >= 0; i--) {
            result.add(ori.get(i));
        }
        return result;
    }
}
