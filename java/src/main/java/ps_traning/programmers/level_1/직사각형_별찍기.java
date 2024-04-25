package ps_traning.programmers.level_1;

import java.util.Scanner;

public class 직사각형_별찍기 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < a; i++) {
            sb.append("*");
        }

        for (int i = 0; i < b; i++) {
            System.out.println(sb.toString());
        }
    }
}
