package ps_traning.algostudy._250819.programmers;

import java.util.*;

class No_43164 {

    public static void main(String[] args) {
        No_43164 sol = new No_43164();
        sol.solution(new String[][]{{"ICN", "JFK"}, {"HND", "IAD"}, {"JFK", "HND"}});
        sol.solution(new String[][]{
                {"ICN", "SFO"},
                {"ICN", "ATL"},
                {"SFO", "ATL"},
                {"ATL", "ICN"},
                {"ATL", "SFO"}
        });
        sol.solution(new String[][]{
                {"ICN", "BBB"},
                {"BBB", "ICN"},
                {"ICN", "AAA"}
        });
    }

    public String[] solution(String[][] tickets) {
        String[] answer = new String[tickets.length + 1];
        Arrays.sort(tickets, (a, b) -> {
            if (a[0].equals(b[0])) return a[1].compareTo(b[1]);
            return a[0].compareTo(b[0]);
        });

        Map<String, List<String>> map = new HashMap<>();
        for (int i = 0; i < tickets.length; i++) {
            String key = tickets[i][0];
            String value = tickets[i][1];
            if (!map.containsKey(key)) map.put(key, new ArrayList<>());
            map.get(key).add(value);
        }

        Map<String, boolean[]> visited = new HashMap<>();
        for (String key : map.keySet()) {
            visited.put(key, new boolean[map.get(key).size()]);
        }

        dfs(tickets.length + 1, 0, "ICN", map, visited, answer);
        System.out.println(Arrays.toString(answer));
        return answer;
    }

    private boolean dfs(int limit, int depth, String cur,
                        Map<String, List<String>> map, Map<String, boolean[]> visited, String[] answer) {
        answer[depth] = cur;
        if (depth + 1 == limit) return true;

        boolean result = false;
        if (!map.containsKey(cur)) return result;
        for (int i = 0; i < map.get(cur).size(); i++) {
            if (visited.get(cur)[i]) continue;
            visited.get(cur)[i] = true;
            result = dfs(limit, depth + 1, map.get(cur).get(i), map, visited, answer);
            if (result) break;
            visited.get(cur)[i] = false;
        }
        return result;

    }
}