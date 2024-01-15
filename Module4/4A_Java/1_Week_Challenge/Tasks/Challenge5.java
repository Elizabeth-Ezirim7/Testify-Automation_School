
import java.util.*;
//create an anagram buckets from a given input of array of words {"akka", "akak", "baab", "baba", "bbaa"};
public class Challenge5 {
    public static void main(String[] args) {
        String[] words = {"akka", "akak", "baab", "baba", "bbaa"};
        Map<String, List<String>> anagramBuckets = createAnagramBuckets(words);

        // Print the anagram buckets
        for (List<String> bucket : anagramBuckets.values()) {
            System.out.println(bucket);
        }
    }

    private static Map<String, List<String>> createAnagramBuckets(String[] words) {
        Map<String, List<String>> anagramBuckets = new HashMap<>();

        for (String word : words) {
            // Sort the characters of the word to use as a key for the HashMap
            char[] charArray = word.toCharArray();
            Arrays.sort(charArray);
            String sortedWord = new String(charArray);

            // Check if the key is already in the HashMap
            if (!anagramBuckets.containsKey(sortedWord)) {
                anagramBuckets.put(sortedWord, new ArrayList<>());
            }

            // Add the word to the corresponding bucket
            anagramBuckets.get(sortedWord).add(word);
        }

        return anagramBuckets;
    }


    }
