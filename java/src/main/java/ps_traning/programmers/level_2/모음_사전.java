package ps_traning.programmers.level_2;

import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class 모음_사전 {
    public int solution(String word) {
        int answer = 0;
        Stack<String> st = new Stack<>();
        Map<String, String> map = new HashMap<>();
        map.put("A", "E");
        map.put("E", "I");
        map.put("I", "O");
        map.put("O", "U");
        while (!String.join("", st).equals(word)) {
            answer++;
            if (st.size() != 5) {
                st.push("A");
                continue;
            }
            String temp = st.pop();
            while (temp.equals("U")) temp = st.pop();
            st.push(map.get(temp));
        }
        return answer;
    }
}
