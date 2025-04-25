package ps_traning.solvedAC.class_4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class No_1043 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.valueOf(st.nextToken());
        int m = Integer.valueOf(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int tn = Integer.valueOf(st.nextToken());
        boolean[] checked = new boolean[n + 1];
        Set<Integer> tInfo = new HashSet<>();
        Queue<Integer> q = new LinkedList<>();
        while (st.hasMoreTokens()) {
            int tNum = Integer.valueOf(st.nextToken());
            tInfo.add(tNum);
            checked[tNum] = true;
            q.add(tNum);
        }

        List<Set<Integer>> partys = new ArrayList<>();
        boolean[] partyChecked = new boolean[m];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int pn = Integer.valueOf(st.nextToken());
            Set<Integer> party = new HashSet<>();
            while (st.hasMoreTokens()) {
                party.add(Integer.valueOf(st.nextToken()));
            }
            partys.add(party);
        }

        while (!q.isEmpty()) {
            int num = q.poll();
            for (int i = 0; i < m; i++) {
                if (!partys.get(i).contains(num) || partyChecked[i]) continue;
                partyChecked[i] = true;
                for (int pnum : partys.get(i)) {
                    if (checked[pnum]) continue;
                    checked[pnum] = true;
                    q.add(pnum);
                }
            }
        }

        int answer = 0;
        for (boolean c : partyChecked) {
            if (!c) answer++;
        }
        System.out.println(answer);
    }
}
