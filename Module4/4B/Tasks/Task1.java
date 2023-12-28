public class Task1 {
    public static void main(String[] args) {
        // Check if "racecar" is a palindrome
        String word1 = "racecar";
        boolean isPalindrome1 = isPalindrome(word1);
        System.out.println("\"" + word1 + "\" is a palindrome: " + isPalindrome1);

        // Check if "10801" is a palindrome
        String word2 = "10801";
        boolean isPalindrome2 = isPalindrome(word2);
        System.out.println("\"" + word2 + "\" is a palindrome: " + isPalindrome2);
    }

    // Function to check if a string is a palindrome
    public static boolean isPalindrome(String str) {
        // Remove spaces and convert to lowercase for case-insensitive comparison
        str = str.replaceAll("\\s", "").toLowerCase();

        // Compare the original string with its reverse
        return str.equals(new StringBuilder(str).reverse().toString());
    }
}
