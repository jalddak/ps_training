package ps_traning.programmers.level_3;

import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class 단어_변환 {
    public boolean CheckChange(String current, String word) {
        int len = current.length();
        boolean result = false;
        int flag = 0;
        for (int i = 0; i < len; i++) {
            if (current.charAt(i) != word.charAt(i)) {
                flag++;
                if (flag > 1) break;
            }
        }
        if (flag == 1) result = true;
        return result;
    }

    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        boolean[] visited = new boolean[words.length];
        Queue<WordCnt> q = new LinkedList<>(List.of(new WordCnt(begin, 0)));
        while (!q.isEmpty()) {
            WordCnt info = q.poll();
            if (info.word.equals(target)) {
                answer = info.cnt;
                break;
            }
            for (int i = 0; i < words.length; i++) {
                if (visited[i]) continue;
                if (CheckChange(info.word, words[i])) {
                    q.offer(new WordCnt(words[i], info.cnt + 1));
                    visited[i] = true;
                }
            }
        }

        return answer;
    }

    class WordCnt {
        String word;
        int cnt;

        public WordCnt(String word, int cnt) {
            this.word = word;
            this.cnt = cnt;
        }
    }
}
