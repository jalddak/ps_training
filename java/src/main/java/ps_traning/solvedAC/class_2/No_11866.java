package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class No_11866 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] nk = new int[2];
        int i = 0;
        while (st.hasMoreTokens()) nk[i++] = Integer.valueOf(st.nextToken());
        int n = nk[0];
        int k = nk[1];

        List<Integer> list = new ArrayList<>();
        for (i = 1; i <= n; i++) {
            list.add(i);
        }

        int r = k - 1;
        int x = 0;
        List<String> answer = new ArrayList<>();
        while (!list.isEmpty()) {
            x += r;
            while (x >= list.size()) x -= list.size();
            String temp = String.valueOf(list.get(x));
            list.remove(x);
            answer.add(temp);
        }
        StringBuilder sb = new StringBuilder();
        sb.append("<");
        sb.append(String.join(", ", answer));
        sb.append(">");
        System.out.println(sb.toString());

    }
}
