package ps_traning;

import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;

public class Test {

    public static void main(String[] args) throws IOException {
        System.out.println(1 << 1);
        System.out.println(2 ^ 1);
        System.out.println(Integer.toBinaryString(2));
        int[] a = new int[]{1, 2, 3};

        Queue<Integer> q = new LinkedList<>();

        StringBuilder sb = new StringBuilder();
        sb.append("asd");
        StringBuilder result = new StringBuilder();
        result.append(sb);
        System.out.println(result);
        System.out.println("   3    ");
        System.out.println("   3");
        System.out.println("   3    ");
    }
}
