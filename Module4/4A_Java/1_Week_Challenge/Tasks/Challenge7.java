
//Reverse TestifyAutomation using recursion
public class Challenge7 {
    public static void main(String[] args) {

    String word = "TestifyAutomation";
    String reversed = reverseString(word);

        System.out.println("Original string: " + word);
        System.out.println("Reversed string: " + reversed);
}
    private static String reverseString(String str) {
        // Base case: if the string is empty or has only one character
        if (str.isEmpty() || str.length() == 1) {
            return str;
        }

        // Recursive case: reverse the substring excluding the first character
        return reverseString(str.substring(1)) + str.charAt(0);
    }
}