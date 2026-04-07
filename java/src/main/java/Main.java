import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    private static List<Integer> list = new ArrayList<>();

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        List<Integer> list = new ArrayList<>();
        List<Integer> rList = new ArrayList<>();

        int answer = 0;
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            bs(arr[i], list);
            bs(arr[n - 1 - i], rList);
            result[i] += list.size();
            result[n - 1 - i] += rList.size();
        }

        answer = Arrays.stream(result).max().getAsInt() - 1;

        System.out.println(answer);
    }

    private static void bs(int num, List<Integer> list) {
        int l = -1;
        int r = list.size();

        while (l + 1 < r) {
            int mid = (l + r) / 2;
            if (list.get(mid) < num) l = mid;
            else r = mid;
        }

        if (r == list.size()) list.add(num);
        else list.set(r, num);
    }
}