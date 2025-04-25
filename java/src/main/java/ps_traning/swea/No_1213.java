package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No_1213 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        for (int tc = 1; tc <= 10; tc++) {
            sb.append("#").append(tc).append(" ");
            Integer.valueOf(br.readLine());
            String a = br.readLine();
            String b = br.readLine();

            int cnt = 0;
            for (int i = 0; i < b.length() - a.length() + 1; i++) {
                boolean flag = true;
                for (int j = 0; j < a.length(); j++) {
                    if (a.charAt(j) != b.charAt(i + j)) {
                        flag = false;
                        break;
                    }
                }
                if (flag) cnt++;
            }
            sb.append(cnt).append("\n");
        }
        System.out.print(sb);
    }
}
