package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class No_11053 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        int[] nums = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.valueOf(st.nextToken());
        }

        List<Integer> dp = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            binarySearch(dp, nums[i], -1, dp.size());
        }
        System.out.println(dp.size());
        
    }

    private static boolean check(List<Integer> list, int num, int index) {
        return list.get(index) >= num;
    }

    private static void binarySearch(List<Integer> list, int num, int left, int right) {
        while (left + 1 < right) {
            int mid = (left + right) / 2;
            if (check(list, num, mid)) right = mid;
            else left = mid;
        }
        if (right == list.size()) {
            list.add(num);
            return;
        }
        list.set(right, num);
    }
}
