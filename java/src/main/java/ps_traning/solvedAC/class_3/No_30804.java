package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class No_30804 {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        List<Integer> tang = new ArrayList<>();
        st = new StringTokenizer(br.readLine());
        while (st.hasMoreTokens()) {
            tang.add(Integer.parseInt(st.nextToken()));
        }
        int[] l = new int[10];
        int kind = 0, answer = 0, left = 0, right = 0;
        for (int i = 0; i < n; i++) {
            int current = tang.get(i);
            l[current]++;
            if (l[current] == 1) kind++;
            if (kind > 2) {
                for (int j = left; j < i; j++) {
                    int target = tang.get(j);
                    l[target]--;
                    if (l[target] == 0) {
                        kind--;
                        left = j + 1;
                        break;
                    }
                }
            }
            right = i;
            answer = Math.max(answer, right - left + 1);
        }
        System.out.println(answer);
    }
}
