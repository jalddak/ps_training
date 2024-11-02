package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class No_11650 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        List<int[]> list = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] xy = new int[2];
            int index = 0;
            while (st.hasMoreTokens()) {
                xy[index++] = Integer.valueOf(st.nextToken());
            }
            list.add(xy);
        }
        list.sort(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] != o2[0]) return o1[0] - o2[0];
                else return o1[1] - o2[1];
            }
        });
        StringBuilder sb = new StringBuilder();
        for (int[] xy : list) {
            sb.append(xy[0]).append(" ").append(xy[1]).append("\n");
        }
        System.out.print(sb.toString());

    }
}
