import java.util.Map;
import java.util.TreeMap;

public class FrequencyCount {
    public static void main(String[] args) {
        String text = "THIS IS A TOY CLASSICAL CIPHER EXAMPLE";
        Map<Character, Integer> counts = new TreeMap<>();
        for (char ch : text.toLowerCase().toCharArray()) {
            if (Character.isLetter(ch)) {
                counts.put(ch, counts.getOrDefault(ch, 0) + 1);
            }
        }
        System.out.println(counts);
    }
}
