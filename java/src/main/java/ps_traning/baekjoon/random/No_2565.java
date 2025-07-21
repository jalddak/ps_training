package ps_traning.baekjoon.random;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class No_2565 {
    private static int n, answer;
    private static int[][] edges;

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.valueOf(br.readLine());

        edges = new int[n][2];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            edges[i][0] = Integer.valueOf(st.nextToken());
            edges[i][1] = Integer.valueOf(st.nextToken());
        }

        Arrays.sort(edges, (a, b) -> Integer.compare(a[0], b[0]));
        List<Integer> result = new ArrayList<>();
        binarySearch(result);
        answer = n - result.size();
        System.out.println(answer);
    }

    private static void binarySearch(List<Integer> nums) {
        for (int i = 0; i < n; i++) {
            int l = -1, r = nums.size();
            while (l + 1 < r) {
                int mid = (l + r) / 2;
                if (nums.get(mid) >= edges[i][1]) r = mid;
                else l = mid;

            }
            if (r == nums.size()) {
                nums.add(edges[i][1]);
                continue;
            }
            nums.set(r, edges[i][1]);
        }
    }
}
