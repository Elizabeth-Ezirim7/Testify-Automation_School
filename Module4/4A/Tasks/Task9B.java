package Tasks;

import java.util.Scanner;

public class Task9B {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String userInput;


        do {
            System.out.print("Enter a word: ");
            userInput = scanner.nextLine();

            // Check if the entered word is not "testify"
            if (!userInput.equals("testify")) {
                System.out.println("Try again.");
            }

        }

        while (!userInput.equals("testify"));

        // Close the scanner to avoid resource leak
        scanner.close();

        // Print a message when "testify" is entered
        System.out.println("Nice! You entered 'testify'.");
    }


}
