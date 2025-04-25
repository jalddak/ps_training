package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_1242 {

    private static final Map<Integer, Integer> hashCode = new HashMap<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        hashCode.put(211, 0);
        hashCode.put(221, 1);
        hashCode.put(122, 2);
        hashCode.put(411, 3);
        hashCode.put(132, 4);
        hashCode.put(231, 5);
        hashCode.put(114, 6);
        hashCode.put(312, 7);
        hashCode.put(213, 8);
        hashCode.put(112, 9);

        int tcCnt = Integer.valueOf(br.readLine());
        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("#").append(tc).append(" ");
            StringTokenizer st = new StringTokenizer(br.readLine());
            int n = Integer.valueOf(st.nextToken());
            int m = Integer.valueOf(st.nextToken());

            Set<String> rows = new HashSet<>();
            for (int i = 0; i < n; i++) {
                StringBuilder row = new StringBuilder();
                boolean flag = false;
                for (char c : br.readLine().toCharArray()) {
                    if (c == '0') {
                        row.append("0000");
                        continue;
                    }
                    flag = true;
                    String binary = Integer.toString(Integer.valueOf(String.valueOf(c), 16), 2);
                    for (int k = 0; k < 4 - binary.length(); k++) row.append('0');
                    row.append(binary);
                }
                if (flag) rows.add(row.toString());
            }

            Set<String> codes = new HashSet<>();

            for (String row : rows) {
                StringBuilder code = new StringBuilder();
                List<Integer> check = new ArrayList<>();
                char cur = row.charAt(0);
                int cnt = 1;
                for (char c : row.toCharArray()) {
                    if (cur == c) {
                        cnt += 1;
                        continue;
                    }
                    check.add(cnt);
                    cur = c;
                    cnt = 1;

                    if (check.size() == 4) {
                        int gcdResult = gcd(gcd(check.get(1), check.get(2)), check.get(3));
                        for (int i = 0; i < 4; i++) {
                            check.set(i, check.get(i) / gcdResult);
                        }
                        code.append(hashCode.get(check.get(1) * 100 + check.get(2) * 10 + check.get(3)));
                        check.clear();
                        if (code.toString().length() == 8) {
                            codes.add(code.toString());
                            code.setLength(0);
                        }
                    }
                }
            }

            int result = 0;
            for (String code : codes) {
                int temp = 0;
                int valid = 0;
                for (int i = 0; i < code.length(); i++) {
                    int num = code.charAt(i) - '0';
                    temp += num;
                    if (i % 2 != 0) valid += num;
                    else valid += num * 3;
                }
                if (valid % 10 == 0) result += temp;
            }
            sb.append(result).append("\n");
        }
        System.out.print(sb);
    }

    private static int gcd(int a, int b) {
        if (a < b) {
            int temp = a;
            a = b;
            b = temp;
        }

        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}
