package ps_traning.solvedAC.class_5;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class No_27172_useArr {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] nums = new int[n];
        int[] cnts = new int[1000001];
        Set<Integer> numSet = new HashSet<>();
        for (int i = 0; i < n; i++) {
            int num = Integer.valueOf(st.nextToken());
            nums[i] = num;
            numSet.add(num);
        }

//        Set<Integer> numSet = Arrays.stream(nums).boxed().collect(Collectors.toSet());

        for (int num : nums) {
            for (int target = num * 2; target <= 1000000; target += num) {
                if (!numSet.contains(target)) continue;
                cnts[num] += 1;
                cnts[target] -= 1;
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int num : nums) {
            sb.append(cnts[num]).append(" ");
        }

        System.out.println(sb.toString());
    }
}
