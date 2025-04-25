package ps_traning.swea;

import java.util.Scanner;

public class No_1217 {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int tcCnt = 10;

        for (int tc = 1; tc <= tcCnt; tc++) {
            String result = "#" + tc + " ";
            scan.nextLine();
            int n = scan.nextInt();
            int p = scan.nextInt();
            scan.nextLine();
            result += pow(n, p);
            System.out.println(result);
        }
    }

    private static int pow(int n, int p) {
        if (p == 0) return 1;
        if (p == 1) return n;
        int half = pow(n, p / 2);
        int result = half * half;
        if (p % 2 == 1) result *= n;
        return result;
    }
}
