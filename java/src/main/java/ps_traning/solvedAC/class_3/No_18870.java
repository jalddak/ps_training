package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_18870 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.valueOf(br.readLine());
        List<Integer> nums = new ArrayList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int i = 0;
        while (st.hasMoreTokens()) nums.add(Integer.valueOf(st.nextToken()));
        List<Integer> sortedNums = new ArrayList<>(new HashSet<>(nums));
        sortedNums.sort(Integer::compareTo);
        Map<Integer, Integer> pressNum = new HashMap<>();
        i = 0;
        for (int num : sortedNums) {
            pressNum.put(num, i++);
        }
        StringBuilder sb = new StringBuilder();
        for (int num : nums) {
            sb.append(pressNum.get(num)).append(" ");
        }
        System.out.println(sb.toString());
    }
}
