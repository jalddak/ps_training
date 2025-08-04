package ps_traning;

import java.io.IOException;
import java.util.Arrays;

public class Test {

    public static void main(String[] args) throws IOException {
        String a = "1234123";
        int[] arr = new int[a.length()];

        arr = a.chars().map(c -> c - '0').toArray();
        System.out.println(Arrays.toString(arr));

        String[] split = a.split("");
        System.out.println(Arrays.toString(split));

        System.out.println("test");

    }
}
