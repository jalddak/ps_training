package ps_traning.baekjoon.binary_search;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Set;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class No_10815 {
    private static int n, m;
    private static int[] nums, checked;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.valueOf(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        m = Integer.valueOf(br.readLine());
        st = new StringTokenizer(br.readLine());
        checked = new int[m];
        for (int i = 0; i < m; i++) {
            checked[i] = Integer.parseInt(st.nextToken());
        }

        useSet();
//        useBinarySearch();


    }

    public static void useSet() {
        Set<Integer> set = Arrays.stream(nums).boxed().collect(Collectors.toSet());
        StringBuilder sb = new StringBuilder();
        for (int c : checked) {
            if (set.contains(c)) sb.append(1).append(" ");
            else sb.append(0).append(" ");
        }
        System.out.println(sb);
    }

    public static int binarySearch(int target) {
        int s = 0;
        int e = n;
        while (s + 1 < e) {
            int mid = (s + e) / 2;
            if (nums[mid] <= target) s = mid;
            else e = mid;
        }
        if (nums[s] != target) return 0;
        return 1;
    }

    public static void useBinarySearch() {
        Arrays.sort(nums);
        StringBuilder sb = new StringBuilder();
        for (int c : checked) {
            sb.append(binarySearch(c)).append(" ");
        }
        System.out.println(sb);
    }

}
