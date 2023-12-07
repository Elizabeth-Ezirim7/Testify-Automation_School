package com.Testify;

public class Task6 {
    public static void main(String[] args) {
        String word = "DEMOCRACY";

        String reversedString = reverseString(word);
        // Extract the word "COME" from the reversed string
        String extractedWord = extractWord(reversedString);


        //word to reverse
        System.out.println(word);
        System.out.println(reversedString);
        System.out.println(extractedWord);

    }
    public static String reverseString(String str) {
        // Create a StringBuilder object from the input string
        StringBuilder stringBuilder = new StringBuilder(str);

        // Use the reverse() method to reverse the string
        stringBuilder.reverse();

        // Convert the StringBuilder
        return stringBuilder.toString();
    }

    //
    public static String extractWord(String str) {
        // Check if the input string contains the word "COME"
        if (str.contains("COME")) {
            return "COME";
        } else {
            return "Word not found";
        }
    }

}


