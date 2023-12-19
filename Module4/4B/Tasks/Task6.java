import java.util.*;

//Despite commuting at the peek hours, she was able to keep to time
public class Task6 {
    public static void main(String[] args) {
        String sentence = "Despite commuting at peek hours, she was able to keep to time";
        String[] words = sentence.split("\\s");

        // Check for anagrams in the given sentence
        checkForAnagrams(words);
    }

    private static void checkForAnagrams(String[] words) {
        for (int i = 0; i < words.length - 1; i++) {
            for (int j = i + 1; j < words.length; j++) {
                if (areAnagrams(words[i], words[j])) {
                    System.out.println("Anagram found: " + words[i] + " and " + words[j]);
                }
            }
        }
    }

    private static boolean areAnagrams(String str1, String str2) {
        // Remove spaces and convert to lowercase for comparison
        str1 = str1.replaceAll("\\s", "").toLowerCase();
        str2 = str2.replaceAll("\\s", "").toLowerCase();

        // Check if the sorted characters of both strings are the same
        char[] charArray1 = str1.toCharArray();
        char[] charArray2 = str2.toCharArray();

        Arrays.sort(charArray1);
        Arrays.sort(charArray2);

        return Arrays.equals(charArray1, charArray2);
    }
}
