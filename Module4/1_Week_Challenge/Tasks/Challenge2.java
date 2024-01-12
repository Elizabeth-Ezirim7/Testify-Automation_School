package Tasks;
//I am the best Automation tester
public class Challenge2 {
    public static void main(String[] args) {

        String sentence = "I am the best Automation tester";
        String reversedSentence = reverseWords(sentence);
        System.out.println("Original sentence: " + sentence);
        System.out.println("Reversed sentence: " + reversedSentence);
    }

    private static String reverseWords(String sentence) {
        // Split the sentence into words
        String[] words = sentence.split("\\s");

        // Reverse the words recursively
        reverseWordsArray(words, 0, words.length - 1);

        // Join the reversed words into a sentence
        return String.join(" ", words);
    }

    private static void reverseWordsArray(String[] words, int start, int end) {
        if (start < end) {
            // Swap the words at the start and end positions
            String temp = words[start];
            words[start] = words[end];
            words[end] = temp;

            // Recursively reverse the remaining words
            reverseWordsArray(words, start + 1, end - 1);
        }
    }
}