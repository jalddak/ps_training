package ps_traning.algostudy._250730;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class No_20310 {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String input = br.readLine();

        int zCnt = 0;
        int oCnt = 0;

        for (char c : input.toCharArray()) {
            if (c == '0') zCnt += 1;
            else oCnt += 1;
        }

        char[] result = new char[input.length() / 2];
        int zlimit = zCnt / 2;
        int olimit = oCnt / 2;
        int index = 0;
        for (char c : input.toCharArray()) {
            if (index == result.length) break;
            if (olimit > 0 && c == '1') {
                olimit--;
                continue;
            }
            
            if (c == '0' && zlimit == 0) continue;
            if (c == '0' && zlimit > 0) {
                zlimit--;
            }
            sb.append(c);
            index++;
        }
        System.out.println(sb);

    }
}
