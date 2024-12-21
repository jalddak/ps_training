package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class No_30804_2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int[] tang = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        int i = 0;
        while (st.hasMoreTokens()) tang[i++] = Integer.valueOf(st.nextToken());
        int[] cnts = new int[10];

        int answer = 0, l = 0, r = 0, kind = 0;

        for (i = 0; i < n; i++) {
            cnts[tang[i]]++;
            if (cnts[tang[i]] == 1) kind++;
            if (kind > 2) {
                for (int j = l; j < i; j++) {
                    cnts[tang[j]]--;
                    if (cnts[tang[j]] == 0) {
                        l = j + 1;
                        kind--;
                        break;
                    }
                }
            }
            r = i;
            answer = Math.max(answer, r - l + 1);
        }
        System.out.println(answer);
    }
}
