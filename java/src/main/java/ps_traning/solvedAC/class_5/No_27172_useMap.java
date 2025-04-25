package ps_traning.solvedAC.class_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.StringTokenizer;

public class No_27172_useMap {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] nums = new int[n];
        Map<Integer, Integer> numCnt = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int num = Integer.valueOf(st.nextToken());
            nums[i] = num;
            numCnt.put(num, 0);
        }
        Set<Integer> numSet = numCnt.keySet();

        for (int num : nums) {
            for (int target = num * 2; target <= 1000000; target += num) {
                if (!numSet.contains(target)) continue;
                numCnt.put(target, numCnt.get(target) - 1);
                numCnt.put(num, numCnt.get(num) + 1);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int num : nums) {
            sb.append(numCnt.get(num)).append(" ");
        }

        System.out.println(sb.toString());
    }
}
