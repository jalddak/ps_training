package ps_traning.solvedAC.class_3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.LinkedList;
import java.util.stream.Collectors;

public class No_5430 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int t = Integer.valueOf(br.readLine());
        for (int i = 0; i < t; i++) {
            String p = br.readLine();
            int n = Integer.valueOf(br.readLine());
            String inputNums = br.readLine();
            inputNums = inputNums.substring(1, inputNums.length() - 1);
            String[] inputNumsArray = inputNums.split(",");
            LinkedList<Integer> nums = new LinkedList<>();
            if (!inputNumsArray[0].equals("")) {
                int[] intINA = Arrays.stream(inputNumsArray).mapToInt(Integer::parseInt).toArray();
                nums = new LinkedList<>(Arrays.stream(intINA).boxed().collect(Collectors.toList()));
            }

            int d = 1;
            boolean flag = true;

            for (char cmd : p.toCharArray()) {
                if (cmd == 'R') {
                    d = -d;
                } else if (cmd == 'D') {
                    if (nums.isEmpty()) {
                        flag = false;
                        break;
                    }
                    if (d == 1) {
                        nums.removeFirst();
                    } else if (d == -1) {
                        nums.removeLast();
                    }
                }
            }

            if (flag) {
                if (d == -1) Collections.reverse(nums);
                sb.append("[");
                sb.append(String.join(",", nums.stream()
                        .mapToInt(Integer::valueOf)
                        .mapToObj(String::valueOf)
                        .toArray(String[]::new)));
                sb.append("]");
            } else sb.append("error");
            sb.append("\n");

        }

        System.out.print(sb.toString());
    }
}
