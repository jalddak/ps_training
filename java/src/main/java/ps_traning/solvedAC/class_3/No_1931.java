package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class No_1931 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        List<int[]> times = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            times.add(new int[]{Integer.valueOf(st.nextToken()), Integer.valueOf(st.nextToken())});
        }
        times.sort(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[1] != o2[1] ? o1[1] - o2[1] : o1[0] - o2[1];
            }
        });

        int before = 0;
        int answer = 0;
        for (int[] t : times) {
            if (before <= t[0]) {
                before = t[1];
                answer += 1;
            }
        }
        System.out.println(answer);
    }
}
