package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_2108 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        List<Integer> nums = new ArrayList<>();
        Map<Integer, Integer> cnts = new HashMap<>();
        double sum = 0;
        for (int i = 0; i < n; i++) {
            int num = Integer.valueOf(br.readLine());
            sum += num;
            nums.add(num);
            if (!cnts.containsKey(num)) cnts.put(num, 0);
            else cnts.replace(num, cnts.get(num) + 1);
        }
        nums.sort(Integer::compareTo);

        List<Integer> keys = new ArrayList<>(cnts.keySet());
        keys.sort(Integer::compareTo);
        keys.sort(new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return cnts.get(o2).compareTo(cnts.get(o1));
            }
        });

        int avg = (int) (sum > 0 ? sum / n + 0.5 : sum / n - 0.5);
        System.out.println(avg);
        System.out.println(nums.get(n / 2));
        System.out.println(n == 1 || cnts.get(keys.get(0)) > cnts.get(keys.get(1)) ? keys.get(0) : keys.get(1));
        System.out.println(nums.get(n - 1) - nums.get(0));
    }
}
