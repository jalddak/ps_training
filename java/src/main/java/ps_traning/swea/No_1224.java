package ps_traning.swea;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;
import java.util.Stack;

public class No_1224 {
    public static final Set<Character> buhoSet = new HashSet<>();

    public static void main(String[] args) throws IOException {
        buhoSet.add('(');
        buhoSet.add(')');
        buhoSet.add('+');
        buhoSet.add('*');
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int tcCnt = 10;
        for (int tc = 1; tc <= tcCnt; tc++) {
            sb.append("#").append(tc).append(" ");

            int length = Integer.valueOf(br.readLine());
            String cmd = br.readLine();

            Stack<Integer> nums = new Stack<>();
            Stack<Character> buhos = new Stack<>();

            for (char c : cmd.toCharArray()) {
                if (buhoSet.contains(c)) {
                    buhos.add(c);
                    if (buhos.peek() != ')') continue;
                    buhos.pop();
                    int num = nums.pop();
                    while (!buhos.isEmpty()) {
                        Character pop = buhos.pop();
                        if (pop == '(') break;
                        num += nums.pop();
                    }
                    if (!buhos.isEmpty() && buhos.peek() == '*') {
                        buhos.pop();
                        num *= nums.pop();
                    }
                    nums.push(num);

                } else {
                    int num = c - '0';
                    if (!buhos.isEmpty() && buhos.peek() == '*') {
                        buhos.pop();
                        num *= nums.pop();
                    }
                    nums.push(num);
                }
            }
            sb.append(nums.pop()).append("\n");
        }

        System.out.print(sb);
    }
}
