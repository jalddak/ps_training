import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

import static java.lang.System.exit;

public class Main {

    private static int k, len;
    private static String result;
    private static Set<String> set = new HashSet<>();

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String sNum = st.nextToken();
        len = sNum.length();
        k = Integer.parseInt(st.nextToken());

        int cnt = 0;
        int zeroCnt = 0;
        boolean flag = false;
        for (char c : sNum.toCharArray()) {
            if (c != '0') cnt++;
            else zeroCnt++;
            if (cnt >= 2 || zeroCnt >= 2) {
                flag = true;
                break;
            }
        }
        if (!flag) {
            System.out.println(-1);
            exit(0);
        }

        set.add(sNum);

        for (int t = 0; t < k; t++) {
            Set<String> next = new HashSet<>();
            for (String num : set) {
                for (int i = 0; i < len; i++) {
                    for (int j = i + 1; j < len; j++) {
                        StringBuilder sb = new StringBuilder();
                        for (int a = 0; a < len; a++) {
                            if (a == i) sb.append(num.charAt(j));
                            else if (a == j) sb.append(num.charAt(i));
                            else sb.append(num.charAt(a));
                        }
                        next.add(sb.toString());
                    }
                }
            }

            set = next;
        }

        result = Collections.max(set);
        System.out.println(result);

    }
}