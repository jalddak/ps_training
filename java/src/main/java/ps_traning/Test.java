package ps_traning;

import java.io.IOException;
import java.util.*;

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

        int[] arr = {1, 2, 3, 4, 5};
        int i = 0;
        System.out.println(arr[i++] + " " + i);

        List<Integer> temp = new ArrayList<>(List.of(1, 2, 3, 4, 5));
        temp.remove(2);
        System.out.println(temp.toString());

    }
}
