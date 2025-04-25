package ps_traning;

import java.io.IOException;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class Test {

    public static void main(String[] args) throws IOException {
        Set<String> set = new HashSet<>();
        set.add("123");
        set.add("123");

        System.out.println(Arrays.toString(set.toArray()));

        char a = '1';
        int ten = Integer.valueOf(String.valueOf(a), 16);
        System.out.println("ten = " + ten);
        String binary = Integer.toString(ten, 2);
        System.out.println("binary = " + binary);


    }
}
