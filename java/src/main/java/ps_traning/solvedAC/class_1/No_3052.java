package ps_traning.solvedAC.class_1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class No_3052 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashSet<Integer> s = new HashSet<>();
        for (int i = 0; i < 10; i++) {
            int n = Integer.valueOf(br.readLine());
            s.add(n % 42);
        }
        System.out.println(s.size());
    }
}
