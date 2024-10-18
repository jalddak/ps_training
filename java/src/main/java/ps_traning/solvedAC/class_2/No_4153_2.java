package ps_traning.solvedAC.class_2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No_4153_2 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int[] lens = new int[3];
            int index = 0;
            while (st.hasMoreTokens()) lens[index++] = Integer.valueOf(st.nextToken());
            Arrays.sort(lens);
            if (lens[0] == 0 && lens[1] == 0 && lens[2] == 0) break;
            else if (lens[0] * lens[0] + lens[1] * lens[1] == lens[2] * lens[2]) System.out.println("right");
            else System.out.println("wrong");
        }
    }
}
