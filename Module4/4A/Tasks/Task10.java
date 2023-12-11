package Tasks;

import java.util.Scanner;

public class Task10 {
    public static void main(String[] args) {
        verifyVisitor();
        //Task10 verifyMeth = new Task10();
        //verifyMeth.verifyVisitor();

    }

    public static void verifyVisitor() {

        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter your purpose for visiting the Slack channel: ");
        String userInput = scanner.nextLine();

        if (userInput.equalsIgnoreCase("Testify")) {
            // Welcome message for "Testify" visitors
            System.out.println("Welcome To Testify Trainings.");
        } else {
            // Rejection message for non-"Testify" visitors
            System.out.println("Sorry, you are not authorized for Testify Trainings");
        }
        scanner.close();


    }

}
