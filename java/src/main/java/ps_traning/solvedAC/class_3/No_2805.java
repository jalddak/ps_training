package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_2805 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.valueOf(st.nextToken());
        int m = Integer.valueOf(st.nextToken());
        st = new StringTokenizer(br.readLine());
        Integer[] trees = new Integer[n];
        int i = 0;
        while (st.hasMoreTokens()) {
            trees[i++] = Integer.valueOf(st.nextToken());
        }
        Arrays.sort(trees, (o1, o2) -> o2 - o1);
        int answer = binarySearch(m, trees);
        System.out.println(answer);
    }

    public static int binarySearch(int m, Integer[] trees) {
        int l = 0;
        int r = trees[0];
        while (l + 1 < r) {
            int mid = (l + r) / 2;
            long temp = 0;
            for (int t : trees) {
                if (t <= mid) break;
                temp += t - mid;
            }
            if (temp >= m) l = mid;
            else r = mid;
        }
        return l;
    }
}
