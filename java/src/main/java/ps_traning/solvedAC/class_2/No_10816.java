package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class No_10816 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[n];
        int i = 0;
        while (st.hasMoreTokens()) arr[i++] = Integer.valueOf(st.nextToken());
        int m = Integer.valueOf(br.readLine());
        int[] nums = new int[m];
        st = new StringTokenizer(br.readLine());
        i = 0;
        while (st.hasMoreTokens()) nums[i++] = Integer.valueOf(st.nextToken());

        Map<Integer, Integer> map = new HashMap<>();
        for (int num : arr) {
            map.put(num, map.containsKey(num) ? map.get(num) + 1 : 1);
        }

        StringBuilder sb = new StringBuilder();
        for (int num : nums) {
            sb.append(map.containsKey(num) ? map.get(num) : 0).append(" ");
        }
        System.out.println(sb.toString());
    }
}
